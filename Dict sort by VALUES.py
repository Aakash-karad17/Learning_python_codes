D={}

list1=[]
n=int(input("how many elements you enter in list:"))
x=1

while(x<=n):
       elements=int(input("enter a serial number:"))
       list1.append(elements)
       x+=1
print("The list of serial number is:",list1)


for x in list1:
       print("enter a roll number for this serial number:",x)
       D[x]=int(input())
      
print("The original dict is:",D)

print("\n")
for y in list1:
       print("serial number=",y,"Roll number=",D[y],end="\n")

import operator

sorted_D=dict(sorted(D.items(),key=operator.itemgetter(1) ))
print("\n\nThe sorted dict (VALUES) is:",sorted_D)

for z in sorted_D:
        print("serial number=",z,"Roll number=",sorted_D[z],end="\n")
        
    
