class time:
    def __init__(self,h,m):
        self.hour=h
        self.min=m
        print("The time you entered is:")
        print(self.hour,"H",self.min,"M")
    def add(self,ho,mi,hox,miy,z):
        print("Enter the time to add:")
        print("\n")
        self.ho=ho
        self.mi=mi
        self.hox=hox
        self.miy=miy
        print("The result is")
        if((self.mi+self.miy)>=60):
            self.za=(self.mi+self.miy)//60
            print(self.ho+self.hox+self.za,"H",(self.mi+self.miy)-60,"M")
        else:
            print(self.ho+self.hox,"H",self.mi+self.miy,"M")
    def Displayminute(self):
        print("Display minute method:")
        print(60*(self.ho+self.hox)+(self.mi+self.miy),"minutes")
obj=time(1,2)
obj1=time(2,40)
h1=int(input("Enter the hour"))
m1=int(input("Enter the min:"))
h2=int(input("Enter the hour"))
m2=int(input("Enter the min:"))

obj.add(h1,m1,h2,m2,5)
obj.Displayminute()
h11=int(input("Enter the hour"))
m11=int(input("Enter the min:"))
h22=int(input("Enter the hour"))
m22=int(input("Enter the min:"))

obj1.add(h11,m11,h22,m22,6)

obj1.Displayminute()
