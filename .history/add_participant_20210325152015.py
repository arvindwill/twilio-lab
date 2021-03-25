# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

participant = client.conversations \
    .conversations('CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .participants \
    .create(
         messaging_binding_address='<Your Personal Mobile Number>',
         messaging_binding_proxy_address='<Your purchased Twilio Phone Number>'
     )

print(participant.sid)
