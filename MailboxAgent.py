#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

from Mail import *
from Confidential import *
from Personal import *
from prettytable.colortable import ColorTable, Themes

#They suggested the use of pprint
#pretty print is awful I hate it, it outputs data with ugly brackets makes ui unreadable.

#Im using prettyTable for the ui
#https://pypi.org/project/prettytable/

#For FA.2 you could use
# tablename.addColumn("ID"......
# tablename.addColumn(email.id....

#   =========================================
#                   To Do List
#
#   - When you are done with FA.1 lemme know!! :D
#
#   - FB.5 a, b, c
#       Personal Mail Type


class Mailbox:
    def __init__(self, emailData):
        self.emailData = self.__gen_mailbox(emailData) #List of Mail type objects

    @classmethod
    def __gen_mailbox(cls, emailData):
        mailbox = []
        for e in emailData:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

#   ============================
#              Features A
#   ============================
    # Feature FA.1 ☆☆☆☆☆ Complete
    # Finds the ID and if it exists, returns it in variable gottedMail. Turns to string incase ID is an int
    def get_email(self, m_id):
        gottedMail = []
        for e in self.emailData:
            if str(m_id) == str(e.id):
                gottedMail.append(e)
                return gottedMail
        return gottedMail
    
    # Feature FA.2 ☆☆☆☆☆ Complete
    # Runs FA.1 to figure out whether the ID email does exist. If it doesn't spits out a message and sends user back to menu
    # If an email does exist with that ID, shows that email using prettytable.
    # It also should check and see if there is a conf tag, try ID 2 to see this!
    def show_email(self, m_id):
        showedMail = self.get_email(m_id)
        if not showedMail:
            print("No email found with that ID.")
            input("☆ Press Enter to continue ☆")
            return
        mail_obj = showedMail[0]
        gottedEmail = ColorTable(theme=Themes.OCEAN)
        # If the email has a conf label, output this format
        # Anyhting else, output the other format under the else statement
        # Uses f"" so that it doesn't show the curly brackets
        if mail_obj.tag == "conf":
            gottedEmail.add_column("CONFIDENTIAL", ["CONFIDENTIAL"])
            gottedEmail.add_column("From", [f"{mail_obj.from_email}"])
            gottedEmail.add_column("Date", [f"{mail_obj.date}"])
            gottedEmail.add_column("Subject", [f"{mail_obj.subject}"])
            gottedEmail.add_column("Encrypted Body Text", [f"{mail_obj.body}"])
            gottedEmail.add_column("Flagged?", [f"{mail_obj.flag}"])
        else:
            gottedEmail.add_column("ID", [f"{mail_obj.id}"])
            gottedEmail.add_column("From", [f"{mail_obj.from_email}"])
            gottedEmail.add_column("To", [f"{mail_obj.to_email}"])
            gottedEmail.add_column("Date", [f"{mail_obj.date}"])
            gottedEmail.add_column("Subject", [f"{mail_obj.subject}"])
            gottedEmail.add_column("Tag", [f"{mail_obj.tag}"])
            gottedEmail.add_column("Body", [f"{mail_obj.body}"])
            gottedEmail.add_column("Flag", [f"{mail_obj.flag}"])
            gottedEmail.add_column("Read", [f"{mail_obj.read}"])
        print(gottedEmail)
        input("☆ Press Enter to continue ☆")

    # Feature FA.3 ☆☆☆☆☆ Completed
    # Runs FA.1 to figure out whether the ID email does exist. If it doesn't spits out a message and sends user back to menu
    # If it does exist, uses the ID grabbed to change that emails tag into "bin", making it moved to the bin
    def del_email(self, m_id):
        gottedMail = self.get_email(m_id)
        if not gottedMail:
            print("No email found with that ID.")
            input("☆ Press Enter to continue ☆")
            return
        for e in self.emailData:
            if str(e.id) == str(m_id):
                e.tag = "bin"
                print("Email has been moved to bin.")
                input("☆ Press Enter to continue ☆ ")
                return

    # Feature FA.4 ☆☆☆☆☆ Completed
    # First, using what the user typed as their email to find, we grab the email data and compare all the entires in it and see whether there is a sender with that email
    # Then, we initialise prettyTable and setup the fieldnames to format the output. Depending on how many entries there are in filteredemails, it will make a row per email
    # If there are entries in filteredemails (found a valid from mail), outputs the list with all emails with the from email the user asked for. If there aren't it lets the user know there aren't any of that email in the mailbox.
    def show_filtered_emails(self, frm):
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

    # Feature FA.5 ☆☆☆☆☆ Completed
    # Will be in Confidential.py
  
#   =============================
#              Features B
#   =============================
    # Feature FB.1  ☆☆☆☆☆   Complete
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

    # Feature FB.2  ☆☆☆☆☆   REQUIRES FA.1   ☆☆☆☆☆   Complete
    def mv_email(self, id, tag):
        # get_email(id).tag = tag
        pass

    # Feature FB.3  ☆☆☆☆☆   REQUIRES FA.1   ☆☆☆☆☆   Complete
    def mrk(self, id, mark_type):
        if(mark_type == "READ"):    #Mark Read
            pass
        #   getemail(id).read = True
        elif(mark_type == "FLAG"):  #Flagged
            pass
        #   getemail(id).flag = True

    # Feature FB.4  ☆☆☆☆☆   Complete
    def find(self, date):
        # search though emaildata
        # return list of Mail where Mail.date == date
        returnlist = []
        for e in self.emailData:
            if e.date == date:
                returnlist.append(e)
        return returnlist

    # Feature FB.4  ☆☆☆☆☆   Complete
    def add_email(self,frm, to,date,subject,tag,body):
        #The id is just its position in the list
        #Creates new Mail object with the correct variables and then appends to emailData
        #id, from_email, to_email, date, subject, tag, body, flag, read
        if tag == "conf":
            newMail = Confidential(len(self.emailData), frm, to, date, subject, tag, body, False, False)
        elif tag == "prsnl":
            newMail = Personal(len(self.emailData), frm, to, date, subject, tag, body, False, False)
        else:
            newMail = Mail(len(self.emailData), frm, to, date, subject, tag, body, False, False)
        self.emailData.append(newMail)

#   ==============================
#             Features C
#   ==============================

    # Exit function
    def exit(self):
        print("☆ Closing Mailbox ☆")
        exit()

    # add two emails at the start
    def populatewithbs(self):
        newMail1 = Mail(len(self.emailData), "sh4175w@gre.ac.uk", "kn2470c@gre.ac.uk", "10/11/2025", "This thing on?", "tag1",
                        """Hello? Hello, hello? \nUh, I wanted to record a message for you to help you get settled in on your first night. \nUm, I actually worked in that office before you. \nI'm finishing up my last week now, as a matter of fact. \nSo, I know it can be a bit overwhelming, but I'm here to tell you there's nothing to worry about. \nUh, you'll do fine. So, let's just focus on getting you through your first week, okay?""", False, False)
        self.emailData.append(newMail1)

        newMail2 = Mail(len(self.emailData), "TheScariestSkeleton@gmail.com", "sh4175w@gre.ac.uk", "10/11/2025", "Mwuahahaha", "tag2","""BOO!""", False, False)
        self.emailData.append(newMail2)

        newMail3 = Confidential(len(self.emailData), "YoshikageKira@hotmail.com", "sh4175w@gre.ac.uk", "22/11/2025", "Jon Arbuckle", "conf",
                        """Solve my Killer Queen Bites The Dust Sheer Heart Attacks""", True, True)
        self.emailData.append(newMail3)
        
        newMail4 = Mail(len(self.emailData), "sh4175w@gre.ac.uk", "sh4175w@gre.ac.uk", "22/11/2025", "NOTE TO SELF", "tag3", """Need to buy milk from Tesco on my way home!""", False, True)
        self.emailData.append(newMail4)

    # Choose how you want to search the emails
    def search_choice_menu(self):

        searchChoiceUI = ColorTable(theme=Themes.OCEAN)
        searchChoiceUI.field_names = ["ID", "Function"]
        searchChoiceUI.add_row(["1", "Date"])
        print()
        print(searchChoiceUI)
        function = input("Enter Function: ")

        # Should return a list of searched Mail
        SearchedMail = ChosenSearchFunction(function)

        searchedUI = ColorTable(theme=Themes.OCEAN)
        searchedUI.field_names = ["ID", "From", "To", "Date", "Subject", "Tag", "Body"]
        for e in SearchedMail:
            searchedUI.add_row([e.id, e.from_email, e.to_email, e.date, e.subject, e.tag, e.body])
        print()
        print(searchedUI)
        input("☆ Press Enter to continue ☆")

    # user Input for specifically Searching by Date and ID
    def search_date_menu(self):
        return self.find(input("Enter Date (DD/MM/YYYY): "))

    def search_id_menu(self):
        return self.get_email(input("Enter Mail ID: "))

    # user input procedure for adding an email
    def add_email_procedure(self):
        frm = input("From: ")
        to = input("To: ")
        date = input("Date: ")
        subject = input("Subject: ")
        tag = input("Tag (Use 'conf' to make it confidential or 'prsnl' to make it personal!): ")
        body = input("Body: ")
        self.add_email(frm, to, date, subject, tag, body)
        input("☆ Press Enter to continue ☆")

#   ==============================
#               UI
#   ==============================
#This bit is just for fun

# Search Function switch case
def ChosenSearchFunction(num):
    switch={
        "1": mailbox.search_date_menu,
        }
    return switch.get(num, lambda: "Invalid choice")()

# Function switch case dictionary
# Switches 1 uses lambda, acts as the courier for m_id to show_email
def ChosenFunction(num):
    switch={
        "1": lambda: mailbox.show_email(input("Enter Mail ID: ")),
        "2": mailbox.show_emails,
        "3": mailbox.add_email_procedure,
        "4": mailbox.search_choice_menu,
        "5": lambda: mailbox.del_email(input("Enter Mail ID: ")),
        "6": lambda: mailbox.show_filtered_emails(input("Enter sender email: ")),
        "10": mailbox.exit
        }
    return switch.get(num, lambda: "Invalid choice")()

def mainMenu():

    FunctionChoiceUI = ColorTable(theme=Themes.OCEAN)
    FunctionChoiceUI.field_names = ["ID", "Function"]
    
    FunctionChoiceUI.add_row(["1", "Display A Mail"])
    FunctionChoiceUI.add_row(["2", "Display Mailbox"])
    FunctionChoiceUI.add_row(["3", "Add New Mail"])
    FunctionChoiceUI.add_row(["4", "Search By..."])
    FunctionChoiceUI.add_row(["5", "Delete Email"])
    FunctionChoiceUI.add_row(["6", "Filter by Sender"])
    FunctionChoiceUI.add_row(["10", "Exit"])

    print()
    print(FunctionChoiceUI)
    function = input("Enter Function: ")
    ChosenFunction(function)

#   ============================
#            ENTRY POINT
#   ============================
mailbox = Mailbox("")
mailbox.populatewithbs()

while True:
    mainMenu()