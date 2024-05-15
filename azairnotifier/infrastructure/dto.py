from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import BaseModel


class EmailMessage(BaseModel):
    subject: str
    sender: str
    receiver: str
    content: str
    content_alt: str

    def to_multipart(self) -> MIMEMultipart:
        multipart = MIMEMultipart()
        multipart['From'] = self.sender
        multipart['To'] = self.receiver
        multipart['Subject'] = self.subject
        multipart.attach(MIMEText(self.content_alt, 'plain'))
        multipart.attach(MIMEText(self.content, 'html'))

        return multipart
