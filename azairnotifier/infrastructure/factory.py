from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MIMEMultipartMessageFactory:
    @staticmethod
    def create(
        subject: str,
        sender: str,
        receiver: str,
        content: str,
        content_alt: str,
    ) -> MIMEMultipart:
        multipart = MIMEMultipart()
        multipart['From'] = sender
        multipart['To'] = receiver
        multipart['Subject'] = subject
        multipart.attach(MIMEText(content_alt, 'plain'))
        multipart.attach(MIMEText(content, 'html'))

        return multipart
