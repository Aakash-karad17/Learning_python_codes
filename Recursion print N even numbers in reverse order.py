def even(n):
        
        if(n>0):
               
             if(n%2==0):
                 print(n)
             even(n-1)
x=int(input("Enter the number:"))
even(x)
