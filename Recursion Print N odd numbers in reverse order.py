def odd(n):
        
        if(n>0):
               
             if(n%2==0):
                     pass
             else:
                     print(n)
             odd(n-1) 
x=int(input("Enter the number:"))
print("The reverse order of odd numbers is:")
odd(x)
