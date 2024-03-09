import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import time
import re

import os

from googleapiclient.errors import HttpError


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




while (1):
    lista_param = readEmails()
    if (lista_param[1] != "No new messages." and lista_param != None and lista_param[0] != "no-reply@accounts.google.com"): 
        print(lista_param[1] + " from " + lista_param[0])

        prompt = lista_param[1]

        response = "pollo"

        sendEmail(lista_param[0], response)
        

    time.sleep(3)
    print("slept...")
    
