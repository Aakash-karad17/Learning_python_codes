a1=[]
a=int(input("enter the first range: "))
b=int(input("enter the second range: "))
s=range(a,b)
for x in s:
       for num in range(2,x):
              
              if(x%num==0):
                     break
       else:
         a1.append(x)
print(a1)
len(a1)
print("The total elements is",len(a1))
                   

