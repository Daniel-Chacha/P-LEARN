#set the parent class as a parameter when creating the child class
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def myfunc(self):
        print('Hello my name is ',self.fname,self.lname)

class student(person):
    pass

x=student('Mike','Olsen')
x.myfunc()
