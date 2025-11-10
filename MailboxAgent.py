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

    # user Input for specifically Searching by Date
    def search_date_menu(self):
        return self.find(input("Enter Date: "))

    # user input procedure for adding an email
    def add_email_procedure(self):
        frm = input("From: ")
        to = input("To: ")
        date = input("Date: ")
        subject = input("Subject: ")
        tag = input("Tag: ")
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
def ChosenFunction(num):
    switch={
        "1": mailbox.show_emails,
        "2": mailbox.add_email_procedure,
        "3": mailbox.search_choice_menu,
        "10": mailbox.exit
        }
    return switch.get(num, lambda: "Invalid choice")()

def mainMenu():

    FunctionChoiceUI = ColorTable(theme=Themes.OCEAN)
    FunctionChoiceUI.field_names = ["ID", "Function"]

    FunctionChoiceUI.add_row(["1", "Display Mailbox"])
    FunctionChoiceUI.add_row(["2", "Add New Mail"])
    FunctionChoiceUI.add_row(["3", "Search By..."])
    #ADD FUTURE FUNCTIONS HERE
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