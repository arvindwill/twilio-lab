# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def bulk_sms(recipients):
    try:
            
        # Your Account Sid and Auth Token from twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        for recipient in recipients:
            message = client.messages \
                .create(
                    messaging_service_sid='MGac4d497ea610d2d594292b773bb5d2e4',
                    body='body',
                    to=f'+1{recipient}'
                )

            print(message.sid)
    except TwilioRestException as e:
        print(e)

RECIPIENTS = [1112223333, 2223334444, 3334445555, 1234567890, 9876543210]

    #twilio api:messaging:v1:services:phone-numbers:create --service-sid MGac4d497ea610d2d594292b773bb5d2e4 --phone-number-sid PN18ced0ce3670384d8ae1caebba362345
