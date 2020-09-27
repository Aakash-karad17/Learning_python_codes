# EVEN NUMBER LIST   
n=int(input("enter the range of numbers:"))
a=[]


for x in range(2,n+1):
       if(x%2==0):
         a.append(x)
         total=sum(a)
print(a)
print("sum of range even number n is",total)


#ODD NUMBER LIST
p=int(input("enter the range of odd numbers:"))


w=[]
s=0
for y in range(1,p+1,2):
       w.append(y)
       s=s+y
print("the list of odd numnbers is ",w)

print("sum of range odd numbers is",s)
