from datetime import datetime
from gtts import gTTS
import os
from twilio.rest import Client   # ✅ Add here

# --- Reminders list ---
reminders = [
    {"name": "Grandpa", "time": "08:00", "medicine": "Blood Pressure Tablet"}
]

# --- Kannada voice reminder function ---
def play_kannada_reminder(message):
    tts = gTTS(text=message, lang='kn')
    filename = "reminder.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # Windows (use 'open' for Mac, 'xdg-open' for Linux)

# --- SMS function (Twilio) ---
def send_sms(message, to_number):
    account_sid = "your_account_sid"   # Replace with your real SID
    auth_token = "your_auth_token"     # Replace with your real token
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_="+XXXXXXXXXX",   # Replace with your Twilio number
        to=to_number
    )

# --- Check reminders ---
def check_reminders():
    now = datetime.now().strftime("%H:%M")
    for r in reminders:
        if r["time"] == now:
            message = f"{r['name']} should take {r['medicine']}"
            print("Reminder:", message)
            play_kannada_reminder(message)    # 🎙 Voice reminder
            # send_sms(message, "+91XXXXXXXXXX")   # 📲 SMS (test later)

# --- Main execution ---
if __name__ == "__main__":
    check_reminders()
