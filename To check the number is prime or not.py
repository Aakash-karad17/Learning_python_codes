num=int(input("enter the number:"))

if(num<2):
    print("the number is not prime")
else:
    for i in range(2,num):
        if(num%i==0):
            print(i,"times",num//i,"is",num)
            print("the number is not prime:")
            break
    else:
        print("the number is prime",num)
