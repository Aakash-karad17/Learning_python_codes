#TO CALCULATE THE FACTORIAL BY USER INPUT
n=int(input("Enter the number to calculate the factorial: "))
x=1
fact=1
if(n==1):
    print("the factorial is 1:")
else:
    while(x<=n):
         fact=fact*n
         n=n-1
print("The factorial is",fact)
