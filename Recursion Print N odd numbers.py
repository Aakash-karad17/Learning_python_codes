def odd(n):
        
        if(n>0):
             odd(n-1)  
             if(n%2==0):
                     pass
             else:
                     print(n)
             
x=int(input("Enter the number:"))
odd(x)
