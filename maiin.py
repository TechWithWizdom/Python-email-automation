
import smtplib
import os

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

sender_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

receiver_email = "johnblessingmartha@gmail.com"

message = EmailMessage()

message["Subject"] = "Welcome to Our Business"
message["From"] =  sender_email
message["To"] = receiver_email

message.set_content(
    "Hello! Welcome to Our Business. "
    "Thank you for choosing us."
)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()

    server.login(sender_email, password)

    server.send_message(message)

print("Email sent successfully!")