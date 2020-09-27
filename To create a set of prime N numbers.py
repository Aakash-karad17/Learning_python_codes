a=int(input("enter a number to gets n prime numbers in sets:"))
b=int(input("enter a second range:"))
s=range(a,b)

s1=set()
for x in s:
     for num in range(2,x):
          if(x%num==0):
               break
     else:
          s1.add(x)
print("The set of prime number is:",s1)
