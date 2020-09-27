class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showName(self):
        print("Name is=",self.name)
    def showAge(self):
        print("Age is:",self.age)
class student(person):
    def __init__(self,r):   #(self,r,n,a)
        person.__init__(self,"Aakash",18)  #(self,n,a)
        self.rollno=r  
        
    def showRollno(self):
        print("Roll no=",self.rollno)


s1=student(201)  #(201,Aakash,18)
s1.showRollno()
s1.showName()
s1.showAge()
