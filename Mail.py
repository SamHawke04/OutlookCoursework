class Mail:
    def __init__(self, text, subject, from_email, to_email):
        self.text = text
        self.subject = subject
        self.from_email = from_email
        self.to_email = to_email

class Confidential(Mail):
    def __init__(self, text, subject, from_email, to_email):
        super().__init__(text, subject, from_email, to_email)

class Personal(Mail):
    def __init__(self, text, subject, from_email, to_email):
        super().__init__(text, subject, from_email, to_email)

