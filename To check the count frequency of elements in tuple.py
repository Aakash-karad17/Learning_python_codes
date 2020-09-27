
n=eval(input("enter a tuple"))
i=0
print("The counting frequency of elements are:")
for x in n:
      if(n.index(x)==i):
          print(x,"-",n.count(x))
    
      i=i+1
print("The total number of elements in a tuple are:")

s1=tuple()
q=0
for y in n:
     if(n.index(y)==q):
         s1=s1+(y,)
         q+=1
print(s1)



print("The length of tuple you entered is:",len(n))



