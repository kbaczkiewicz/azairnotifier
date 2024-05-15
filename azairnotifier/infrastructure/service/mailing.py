import smtplib
import ssl
from azairnotifier.application.service.mailing import Mailer
from infrastructure.factory import MIMEMultipartMessageFactory


class SimpleSMTPMailer(Mailer):
    smtp_server: str
    port: int
    sender_email: str
    sender_password: str

    def __init__(self, smtp_server: str, port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email: str, subject: str, content: str, content_alt: str) -> None:
        message = MIMEMultipartMessageFactory.create(subject, self.sender_email, receiver_email, content, content_alt)
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=ssl.create_default_context()) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(
                self.sender_email, receiver_email, message.as_string()
            )
