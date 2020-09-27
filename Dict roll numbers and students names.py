items={}


list1=[]

n=int(input("how many roll numbers you want:"))
x=1
while(x<=n):
     elements=int(input("\nEnter the roll number:"))

     list1.append(elements)
     x+=1
print("\n\nThe list of Roll numbers you enter is:",list1)



for y in list1:
         print("\nEnter name for this roll number:",y)

         items[y]=input()
print("\nThe Dict is:",items)



print("\n\n")
for z in list1:
        
         print("(",z,",",items[z],")",end=",") # EACH ITEMS IN ONE LINE


print("\n\n")


for p in list1:
     print("Roll number=",p,"Student Name=",items[p],end="\n")
