items={}



list1=[201,202,203,204,205]


for x in list1:
      print("enter a name for ",x)

      items[x]=input()
print("\n\nThe original dict is:",items)

print("\n\n\n")
for y in items:
      print("(",y,",",items[y],")",end="\n")
