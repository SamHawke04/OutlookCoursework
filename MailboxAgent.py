#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """<This is the documentation for MailboxAgent. All methods defined in this class are used to manage the mailbox containing emails represented as Mail objects.>"""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox
    
    def getemail_data(self):
        return self._mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
        gottedMail = []
        for e in self._mailbox.email_data:
            if str(m_id) == str(e.id):
                gottedMail.append(e)
                return gottedMail
        return gottedMail

    # FA.3
    # 
    def del_email(self, m_id):
        gottedMail = self.get_email(m_id)
        if not gottedMail:
            print("No email found with that ID.")
            input("☆ Press Enter to continue ☆")
            return
        for e in self.email_data:
            if str(e.id) == str(m_id):
                e.tag = "bin"
                print("Email has been moved to bin.")
                input("☆ Press Enter to continue ☆ ")
                return

    # FA.4
    # 
    def filter(self, frm):
        filteredemails = [e for e in self.emailData if str(frm) == str(e.from_email)]       
        table = ColorTable(theme=Themes.OCEAN)
        table.field_names = ["ID", "From", "To", "Date", "Subject", "Tag", "Body"]
        for e in filteredemails:
            table.add_row([e.id, e.from_email, e.to_email, e.date, e.subject, e.tag, e.body])
        print()
        if filteredemails:
            print(table)
        else:
            print("No emails found from that sender...")
        input("☆ Press Enter to continue ☆ ")

    # FA.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        #Creates Table
        showEmailUI = ColorTable(theme=Themes.OCEAN)
        showEmailUI.field_names = ["ID", "From", "To", "Date", "Subject", "Tag", "Body"]

        #Loops through all email data and adds:
        #ID, from, to, date, subject, tag, body
        #All into a row
        #then to show the Table you simply print it
        for e in self.emailData:
            showEmailUI.add_row([e.id, e.from_email, e.to_email, e.date, e.subject, e.tag, e.body])

        print()
        print(showEmailUI)
        input("☆ Press Enter to continue ☆")

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        self.get_email(m_id).tag = tag

    # FB.3
    # 
    def mark(self, m_id, m_type):
        if(m_type == "READ"):    #Mark Read
           self.getemail(m_id).read = True
        elif(m_type == "FLAG"):  #Flagged
            self.getemail(m_id).flag = True

    # FB.4
    # 
    def find(self, date):
        # search though emaildata
        # return list of Mail where Mail.date == date
        returnlist = []
        for e in self.email_data:
            if e.date == date:
                returnlist.append(e)
        return returnlist

    # FB.5
    # 
    def sort_from(self):
        """  """
        pass


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        # code must generate unique m_id
        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                newMail = Confidential(len(self.emailData), frm, to, date, subject, tag, body, False, False)
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                newMail = Personal(len(self.emailData), frm, to, date, subject, tag, body, False, False)
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                newMail = Mail(len(self.emailData), frm, to, date, subject, tag, body, False, False)
        self.emailData.append(newMail)