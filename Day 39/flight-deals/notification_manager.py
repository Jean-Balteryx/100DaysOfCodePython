from twilio.rest import Client
import smtplib
import requests

ACCOUNT_SID = "ACeb1b8f647238fb1313e69c2ebdd37f50"
AUTH_TOKEN = "0d2d81fa63b8dbcc8a58b9c725e359aa"
MY_EMAIL = "dummy@gmail.com"
MY_PASSWORD = "password"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_alert(self, body):
        message = self.client.messages \
            .create(
            body=body,
            from_='+15863718448',
            to='+33665708618'
        )
        print(message.status)

    def send_emails(self, emails, message, link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode('utf-8')
                )
