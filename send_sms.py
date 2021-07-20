import os
from twilio.rest import Client

account_sid = 'AC09f2eccf9b8f09110f362adf2af7f297'
auth_token = '8babbfd8241f6b4f372a33dd29660173'
client = Client(account_sid, auth_token)


def send_message():
    client.messages.create(
        to="+573185886509",
        from_="+15878408138",
        body="Corona esta llegando hacia ti, prepárate!"
    )