def fab(n):
        if(n<=1):
            return n
        else:
            return (fab(n-1)+fab(n-2))


a=int(input("Enter how many terms:"))


if(a<=0):
    print("Enter the positive number:")
else:
    print("Fibonnaci series are:")
    for i in range(a):
        print(fab(i),end=",")


