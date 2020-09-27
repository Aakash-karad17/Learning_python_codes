a=[]

n=int(input("how many elements"))

s=0
for x in range(0,n):
       elements=int(input("enter the elements: "))
       a.append(elements)
       s=s+int(elements) # YOU CAN ALSO WRITE SUM KEYWORD:
                         # total=sum(a) a:- is the list name   
print(a)                  
print("the sum is",s)



