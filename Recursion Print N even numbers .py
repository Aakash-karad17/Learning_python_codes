def even(n):
        
        if(n>0):
             even(n-1)   
             if(n%2==0):
               print(n)

x=int(input("Enter the number:"))
even(x)
