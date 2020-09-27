def gcd(a,b):
       if(a<b): 
           smaller=a
       else:
           smaller=b
    
       for p in range(1,smaller+1):
               if((a%p==0)and(b%p==0)):
                       hcf=p
                       

       print("The gcd of two number is:",hcf)


x=int(input("Enter a number:"))
y=int(input("Enter a number:"))

gcd(x,y)

