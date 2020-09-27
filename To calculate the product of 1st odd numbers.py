n=int(input("enter the number"))
x=1
pro=1
if(n==0):
    print("The product is zero")
else:
    while(x<=n):
        print(x)
        pro=pro*x
        x=x+2
print("the product of first odd numbers is",pro)
