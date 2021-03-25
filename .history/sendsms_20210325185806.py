# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


try:
        
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            messaging_service_sid='MG9752274e9e519418a7406176694466fa',
            body='body',
            to='+15558675310'
        )

    print(message.sid)
except TwilioRestException as e:
    print(e)