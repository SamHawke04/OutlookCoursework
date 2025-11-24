#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FB.5.a
class Personal():
    """ """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec
    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY
        pass

    # FB.5.b
    #
    def add_stats(self):
        #Find @ in mail.frm
        for index, character in enumerate(self.frm):
            if character == "@":
                UserID = self.frm[:index]
        
        #Get rid of "Body" in subject
        self.subject[3:]
        
        #Find Longest Word
        #Find Average
        #Find wordCount
        for index, chara in enumerate(self.body):
            if chara == " ":
                Averagelen =+ Counter
                Counter = 0
                wordCount =+ 1
            else:
                Counter =+ 1
                if Counter > longwordleng:
                    longwordleng = Counter
        Averagelen = Averagelen / wordCount

        #Add stats to body
        self.body = UserID+self.body+" Stats: Word Count: "+wordCount+", Average word length: "+Averagelen+", Longest word length: "+longwordleng+"."
