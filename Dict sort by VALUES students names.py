d={}
list1=[]

n=int(input("how many elements:"))
x=1
while(x<=n):
     elements=int(input("enter a roll number:"))
     list1.append(elements)
     x+=1

print("The list is:",list1)


for x in list1:
     print("enter the name for this roll number:",x)
     d[x]=input()
print("\nThe original dict is:",d)

import operator
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1)))

print("\nThe sorted dict is:\n",sorted_d)

print("\n\n")
for y in sorted_d:
         print("roll number:",y,"Name:",sorted_d[y],end="\n")
