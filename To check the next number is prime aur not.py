a=int(input("enter the number: "))
b=int(input("enter the number: "))


for x in range(a,b):
    for num in range(2,x):
           if(x%num==0):
               print(x,"not prime\n")
               break
    else:
       print(x,"is prime\n")
    
