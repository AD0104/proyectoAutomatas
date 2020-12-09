import re
class Regex:
    #Global variable to set the regex
    regex = "" 
    def __init__(self):
        print("created object")

    def set_regex(self,new_regex):
        #with self.var_name we call the global variable.
        self.regex = new_regex

    def get_regex(self):
        return self.regex

    def verify_text(self, text):
        return re.search("^[a|b|c][c][a]+$",text)
r = Regex()
print(r.get_regex())
r.set_regex("new regex")
print(r.get_regex())
if r.verify_text("acaaaa"):
    print("match found")
else:
    print("no match found")
