def lcm(a,b):
     if(a>b):
          greater=a
     else:
          greater=b

     while(True):
           if((greater%a==0) and (greater%b==0)):
                lcm=greater
                return lcm            # RETURN SOMETHING
                break
           else:
                greater=greater+1
     #print("The LCM is:",lcm)

     
x=int(input("enter 1st number:"))
y=int(input("enter 1st number:"))                
p=lcm(x,y)
print("The LCM is:",p)
