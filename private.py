class myClass:
    __privateever = 27 ;
    def _privleth(self):
        print("im inside my class")
    def hello(self):
        print("private varible vale: ",myClass.__privateVar)
foo = myClass
foo.hello
foo._privleth