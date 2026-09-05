class IOString():
    def __init__(self):
        self.strl = ""
    def get_String(self):
        self.strl = ("enter string : ")
    def print_String(self):
        print("reult is :"self.strl.upper())
strl= IOString()
strl.get_String()
strl.print_String()