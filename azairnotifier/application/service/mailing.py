import abc


class Mailer(abc.ABC):
    def send_email(self, receiver_email: str, subject: str, content: str, content_alt: str) -> None:
        pass
