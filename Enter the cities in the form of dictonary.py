a=input("enter the city:")
b=input("enter the second city:")
c=input("enter the third city:")
if(a<b<c):
 print(a,b,c)
elif(b<c<a):
 print(b,c,a)
elif(c<a<b):
    print(c,a,b)
elif(a<c<b):
    print(b,c,a)
elif(b<a<c):
    print(b,a,c)
elif(c<b<a):
    print(c,b,a)




# SECOND METHOD
"""
x=input()
y=input()
z=input()
q=min(x,y,z)
print(q)
if(q==x):
 print(min(y,z))
 print(max(y,z))
elif(q==y):
  print(min(x,z))
  print(max(x,z))
elif(q==z):
  print(min(x,y))
  print(max(x,y))
"""
