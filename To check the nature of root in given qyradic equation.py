print("The equation are Ax**2+By+C=0")
a=int(input("enter A:"))
b=int(input("enter B:"))
c=int(input("enter C:"))
d= b**2-4*a*c
d1=d**0.5
if(d<0):
 print("the root are imaginary")
elif(d>0):
    x1=(-b+d1)/(2*a)
    x2=(-b-d1)/(2*a)
    print("the x1 point is %f" %x1)
    print("the x2 point is %f" %x2)
    print("the roots are unequal and real")
elif(d==0):
    x1=(-b+d1)/(2*a)
    x2=(-b-d1)/(2*a)
    print("the x1 point is %f" %x1)
    print("the x2 point is %f" %x2)
    print("the roots are equal and real")
