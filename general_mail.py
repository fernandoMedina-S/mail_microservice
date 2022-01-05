import smtplib, ssl
import dotenv
import os

#loading the env file
dotenv.load_dotenv(".env")

sender = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def main(receiver, message):
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
        return {"status": "Success"}
    except:
        return {"status": "Failed"}

