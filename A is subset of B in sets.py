a=eval(input("Enter a first set:"))

b=eval(input("Enter a second set:"))

y=set(b).issubset(a)
z=set(a).issubset(b)
if(z==True):
     print("a is sub set b")

elif(y==True):
     print("b is sub set of a")
else:
     print("a is not subset of b")
     print("b is not subset of a ")

