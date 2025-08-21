from twilio.rest import Client
from dotenv import load_dotenv
import os

# load .env variables
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! 🚀 This is a test SMS from Twilio.",
    from_=from_number,
    to="+XXXXXXXXXX"
)

print("✅ Message sent! SID:", message.sid)
