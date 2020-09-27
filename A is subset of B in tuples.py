
a=eval(input("enter a tuple:"))
b=eval(input("enter a tuple: "))


print("The original 1st tuple is:",a)
print("The original 2nd tuple is:",b)



r1=set(a).issubset(b)

r2=set(b).issubset(a)

print("A is subset of B is:",r1)
print("B is subset of A is:",r2)
