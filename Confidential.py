#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# Feature FA.5 ☆☆☆☆☆ Completed
# Since this one is a tad bit more complicated, I'll comment on the lines of code where necessary
from Mail import Mail

class Confidential(Mail):
    def __init__(self, id, from_email, to_email, date, subject, tag, body):
        super().__init__(id, from_email, to_email, date, subject, tag, body)
        self.body = self.encrypt(body)  # Encrypt message body on creation


    def encrypt(self, message):
        words = message.split()   # split into words
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