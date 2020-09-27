n=int(input("How many elements in the sets:"))
a1=[]
q=0
x=1
while(x<=n):
     elements=int(input("enter a elements:"))
     a1.append(elements)
     x=x+1




s1=set(a1)
print("This is set:",s1,type(s1))

print("The counting elements in sets are:")

for y in a1:
     if(a1.index(y)==q):
          print(y,"-",a1.count(y))
     q=q+1

print("The length of sets are:",len(s1))
