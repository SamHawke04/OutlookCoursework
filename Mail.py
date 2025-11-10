class Mail:
    def __init__(self, id, from_email, to_email, date, subject, tag, body, flag, read):
        self.id = id
        self.from_email = from_email
        self.to_email = to_email
        self.date = date
        self.subject = subject
        self.tag = tag
        self.body = body
        self.flag = flag
        self.read = read

    def getAll(self):
        return self.id, self.from_email, self.to_email, self.date, self.subject, self.tag, self.body, self.flag, self.read

class Confidential(Mail):
    def __init__(self, from_email, to_email, date, subject, tag, body):
        super().__init__(from_email, to_email, date, subject, tag, body)

class Personal(Mail):
    def __init__(self, from_email, to_email, date, subject, tag, body):
        super().__init__(from_email, to_email, date, subject, tag, body)


