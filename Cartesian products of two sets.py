
list1=[eval(x) for x in input().split(" ")]

list2=[eval(x) for x in input().split(" ")]

n=int(input("enter a number in order of cartesian product:"))

n1=len(list1)
n2=len(list2)



for i in range(0,n):   # zero because of indexing loop.
      for j in range(0,n1):
          print("(",list1[i],","," ",list2[j],")",sep="",end=" ")
          


"""

A=[eval(x) for x in input().split(" ")]
B=[eval(x) for x in input().split(" ")]

A.sort()
A1=[]
i=0

for y in A:
    if(A.index(y)==i):
        A1.append(y)
    
    i+=1

A1.sort()

B.sort()
B1=[]
m=0

for y in B:
    if(B.index(y)==m):
        B1.append(y)
    
    m+=1

B1.sort()

#cartesian product
l1=len(A1)
l2=len(B1)

for j in range(0,l1):
    for k in range(0,l2):
        print("(%d, %d)" % (A1[j],B1[k]), end=" ")
"""
