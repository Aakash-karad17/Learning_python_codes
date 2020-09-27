n=eval(input("enter a tuple:"))



print("The orignal tuple is",n)


sum=0


for x in n:
       for y in x:
           sum=sum+y
           result=sum/len(n)
print("The average of tuple is:",result)
