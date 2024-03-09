from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import base64

# Set up API credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']
creds = None
flow = InstalledAppFlow.from_client_secrets_file('client_secret_141561675916-3pqnujne4ji7j873q6u57gv6ajhrisep.apps.googleusercontent.com.json', SCOPES)
creds = flow.run_local_server(port=5000)

# Connect to Gmail API
service = build('gmail', 'v1', credentials=creds)

# Get the email by ID (replace 'YOUR_EMAIL_ID' with the actual email ID)
email_id = 'unoxbot@gmail.com'
message = service.users().messages().get(userId='me', id=email_id).execute()

print("received message: " + message)

# Process content (replace this with your processing logic)
subject = message['subject']
body = base64.urlsafe_b64decode(message['payload']['body']['data']).decode('utf-8')

# Compose reply
reply_subject = f"Re: {subject}"
reply_body = "Your reply content goes here."

# Create MIMEText object for the reply
reply_message = MIMEText(reply_body)
reply_message['to'] = message['payload']['headers'][0]['value']  # Replace with sender's email address
reply_message['subject'] = reply_subject

# Encode the message to base64
raw_message = base64.urlsafe_b64encode(reply_message.as_bytes()).decode('utf-8')

# Send the reply
service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
