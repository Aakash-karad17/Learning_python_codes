items={}

list1=[]
n=int(input("How many roll numbers:"))
x=1
while(x<=n):
    elements=int(input("enter a number:"))
    list1.append(elements)
    
    x=x+1

print("\n\n")
for y in list1:
      print("enter name for",y)
      items[y]=input()
print("The original dict you entered is:",items)




for p,q in items.items():
        print("keys=",p,"\t","values=",q,)
        


print("\n\nthe sorted dict (KEYS) is:")
list1.sort()
for z in list1:
    print("{",z,":",items[z],"}",end=",")


#Values-sorted



print("\n\n The sorted by values:\n\n")
for w in sorted(items,key=items.get):
        print("{",w,":",items[w],"}",end=",")
