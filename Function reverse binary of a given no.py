def revbinary(a):
     
     b=bin(a)
     print("The binary is:",b[2::])
     print("The reverse binary is:",b[2::-1])
x=int(input("Enter the integer to print binary no:"))
revbinary(x)

