#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FA.5.a
class Confidential():
    """ """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id,frm,to,date,subject,tag,body):    # DO NOT MODIFY Attributes
        super().__init__(m_id,frm,to,date,subject,tag,body)   # Inherits attributes from parent class DO NOT MODIFY
        pass

    # FA.5.b
    #
    def encrypt(self):
        words = self.body.split()   # split into words
        word_count = len(words)
        result = []
        for word in words: # loop for amount of word in body of email
            encrypted_word = ""
            for char in word: # this loops for amount of characters in word!
                if char.isalpha():
                    # Make lowercase to handle both cases, get position (a=1, b=2, until y=25, z=26)
                    pos = ord(char.lower()) - ord('a') + 1
                    encrypted_word += str(pos * word_count)
                elif char.isdigit():
                    # Thia converts digits to a letter (0=a, 1=b, until 8=i, 9=j)
                    encrypted_word += chr(ord('a') + int(char))
                elif char == '.':
                    encrypted_word += '.' # keep the full stop as is
                else:
                    encrypted_word += char
            result.append(encrypted_word) # We mash it together and output a lovely ciphered body!
        return " ".join(result) # return the body here