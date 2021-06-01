import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client("ACc8256a5476096c529a458fb3a748673e", "982427fdf4477c6eb265f25c7f03dc0a")

message = client.messages \
                .create(
                     body="Happy Birthday Yashwanth",
                     from_='+14159934127',
                     to='+919080651923'
                 )

print(message.sid)
