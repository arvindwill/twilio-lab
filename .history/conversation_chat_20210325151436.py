# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations('CH806cd750675141c2a5d1717b206f5d76') \
                     .fetch()

print(conversation.chat_service_sid)


# ISc0c7e815ffe74545b3819d5efd57147a