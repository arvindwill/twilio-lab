# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def bulk_sms(country_code,recipients):
    try:
            
        # Your Account Sid and Auth Token from twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        for recipient in recipients:
            recipient = recipient.replace("-","")
            try:
                message = client.messages \
                    .create(
                        messaging_service_sid='MGac4d497ea610d2d594292b773bb5d2e4',
                        body='body',
                        to=f'{country_code}{recipient}'
                    )
                print(message.sid)
            except TwilioRestException as e:
                print(e)        
    except TwilioRestException as e:
        print(e)


RECIPIENTS = ['111-222-3333', '222-333-4444', '333-444-5555', '123-456-7890', '987-654-3210']
bulk_sms('+1',RECIPIENTS)
RECIPIENTS = ['98940-94852']
bulk_sms('+91',RECIPIENTS)
    #twilio api:messaging:v1:services:phone-numbers:create --service-sid MGac4d497ea610d2d594292b773bb5d2e4 --phone-number-sid PN18ced0ce3670384d8ae1caebba362345
