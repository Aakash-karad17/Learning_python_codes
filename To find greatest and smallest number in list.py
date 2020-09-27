a=[]
n=int(input("how many elements: "))

for x in range(0,n):
      elements=int(input("enter the elements"))
      a.append(elements)
      a.sort()
print(a[-1],"is greatest no")
print(a[0],"is smallest no")

