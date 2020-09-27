def sum1(n):
       x=1
       while(x<=n):
             print(2*x-1)
             x+=1
  




x=int(input("Enter the number:"))

sum1(x)
#USING RECURSION
def sum1(i,n):
           if(n>=i):        
                 
                 sum1(i+1,n)
                 print(2*i-1)
  




x=int(input("Enter the number:"))

sum1(1,x)
