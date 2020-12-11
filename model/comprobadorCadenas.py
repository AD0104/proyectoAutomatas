import re
class Regex:
    #Global variable to set the regex
    regex = "^[a|b|c][c][a]+$" 
    def __init__(self):
        print("created object")
    def set_regex(self,new_regex):
        self.regex = new_regex
    def get_regex(self):
        return self.regex
    def verify_text(self, text):
        return re.search(self.regex,text)
