s1=int(input("enter the marks in maths (100 out of) :"))
s2=int(input("enter the marks in chemistry (100 out of) :"))
s3=int(input("enter the marks in english (100 out of) :"))
s4=int(input("enter the marks in physics (100 out of) :"))
s5=int(input("enter the marks in computer/IT (100 out of) :"))
S=s1+s2+s3+s4+s5
p=(S*100)/5
P=float(p)
if(s1<33):
    print("FAIL IN MATHS")
elif(s2<33):
    print("FAIL IN CHEMISTRY")
elif(s3<33):
    print("FAIL IN ENGLISH")
elif(s4<33):
    print("FAIL IN physics")
elif(s5<33):
    print("FAIL IN COMP/IT")
elif(S>=400):
    print("PASS")
    print("first division")
    print(P)
elif(S>=300):
    print("PASS")
    print("second division")
    print(P)
elif(S>=165):
    print("PASS")
    print("third division")
    print(P)
    
