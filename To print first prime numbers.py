

a=int(input("enter the number:"))

b=int(input("enter the number:"))


s=range(a,b)


for x in s:
    for num in range(2,x):
        if(x%num==0):
            break
    else:
        print(x,"is the prime number") 
        break    # IT IS USED TO PRINT ONLY ONE NEXT PRIME NUMBER OF A RANGE
