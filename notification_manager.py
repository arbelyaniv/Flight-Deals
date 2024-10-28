import os
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    # option to send message
    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        print(message.sid)

    # option to send whatsapp
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)