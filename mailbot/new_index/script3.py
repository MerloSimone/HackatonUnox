import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import time
import re
import boto3
import json

import sys
sys.path.append('..')

# Use absolute import for bot_lib
import bot_lib as bot

import streamlit as st
from email.mime.text import MIMEText
from email.message import EmailMessage
from requests import HTTPError


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

def extract_email(input_string):
    pattern = r'<(.*?)>'
    match = re.search(pattern, input_string)
    
    if match:
        return match.group(1)
    else:
        return None

def readEmails():
    
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(               
                # your creds file here. Please create json file as here https://cloud.google.com/docs/authentication/getting-started
                'secret.json', SCOPES)
            creds = flow.run_local_server(port=5000)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
        messages = results.get('messages',[])
        if not messages:
            return ['', 'No new messages.']
        else:
            message_count = 0
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()                
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    if name == 'From':
                        from_name= values['value']                
                        for part in msg['payload']['parts']:
                            try:
                                data = part['body']["data"]
                                byte_code = base64.urlsafe_b64decode(data)

                                text = byte_code.decode("utf-8")
                                #print ("This is the message: "+ str(text))
                                msg  = service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()          
                                lista_param = []     
                                lista_param.append(extract_email(str(from_name)))
                                lista_param.append(str(text))
                                return lista_param
                            
                                # mark the message as read (optional)
                            except BaseException as error:
                                pass                            
    except Exception as error:
        print(f'An error occurred: {error}')

def sendEmail(recipient, response):
    SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token2.json'):
        creds = Credentials.from_authorized_user_file('token2.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(               
                # your creds file here. Please create json file as here https://cloud.google.com/docs/authentication/getting-started
                'secret.json', SCOPES)
            creds = flow.run_local_server(port=5000)
        # Save the credentials for the next run
        with open('token2.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    message = MIMEText(response)
    message['to'] = recipient
    message['subject'] = 'Response to your question'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connected to the database!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def insert_response_into_database(connection, sender_email, email_content, chatbot_response):
    if connection is not None:
        try:
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO users (email_address)
                VALUES (%s);
            """
            values = []
            values.append(sender_email)
            cursor.execute(insert_query, values)
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()


#db_connection = connect_to_database('89.40.142.15', 'acme_user', 'acme_user', 'unox')
            
def ask_question(response, user_question, modelId='anthropic.claude-v2', max_tokens_to_sample=2048, temperature=0, top_p=0.5):

    
    predetermined_question = ("You are a customer service agent tasked with classifying emails by type, summarize the content and provide a response for than email. "
                          "These are the categories"
                          "product informations;"
                          "Technical Support ; "
                          "Billing and Pricing; "
                          "General Inquiry ; "
                          "Order Status ; "
                          "The response should not include informations about your reasoning be as complete as possible but also writted in a concise way "
                          "Provide your answer in a JSON format reporting a 'Category' field, a 'Summary' a 'Response' field like this:{ \"Category\": \"\", \"Summary\": \"\", \"Response\": \"\" }"
                          "use these informations in the answer: ")
    
    #response_content = gapp.get_rag_response(index=gapp.st.session_state.vector_index, question=gapp.input_text) #call the model through the supporting library
    
    final_question = f"{predetermined_question} {response} {user_question}"
    brt = boto3.client(service_name='bedrock-runtime')

  

    body = json.dumps({
        "prompt": f"\n\nHuman: {final_question}\n\nAssistant:",
        "max_tokens_to_sample": max_tokens_to_sample,
        "temperature": temperature,
        "top_p": top_p,
    })

    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    return response_body.get('completion')



while (1):
    lista_param = readEmails()
    if (lista_param[1] != "No new messages." and lista_param != None and lista_param[0] != "no-reply@accounts.google.com"): 
        print(lista_param[1] + " from " + lista_param[0])

        prompt = lista_param[1]

        st.session_state['chat_type']='email'


        response = bot.get_rag_mail_response(input_text=prompt, index=bot.get_index(),) #call the model through the supporting library
       
        #print(ask_question(response, prompt))
        # Call the function and get the response

        response_json = ask_question(response, prompt)
        
        # Load the response as a Python dictionary
        response_dict = json.loads(response_json)
        
        # Extract the 'response' field
        category = response_dict.get('Category')
        # Extract the 'response' field
        summary = response_dict.get('Summary')
        # Extract the 'response' field
        response = response_dict.get('Response')

        print("Category is: " +category)
        print("Summary is: " +summary)
        print("Response is: " +response)

        

        sendEmail(lista_param[0], response)
        #insert_response_into_database(db_connection, lista_param[0], lista_param[1], response)
        

    time.sleep(3)
    print("slept...")
    
#if db_connection:
 #   db_connection.close()