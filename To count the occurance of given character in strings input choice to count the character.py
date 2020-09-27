n=input("enter the string:")
c=input("enter the character in which you want to count:")

for s in n:
       n.count(c)    # count() INBUILT FUNCTION.
print(n.count(c))




# SECOND METHOD WITH COUNT LOGIC.

z=input("enter the string: ")

c1=input("enter the character in which you want to count:")

count=0

for d in z:
       if(d==c1):
              count=count+1
print(count)
