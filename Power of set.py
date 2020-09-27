n=eval(input("Enter a tuple/list:"))

list1=[]


for x in n:
     if(n.count(x)>2):
          continue
     else:
          list1.append(x)
s1=set(list1)
length=len(s1)

print("The original set is:",s1)

print("The power of set is:",2**length,type(s1))



#SECOND METHOD:



i=eval(input("Enter a tuple:"))

s2=set(i)
print("the power of set is:",2**len(s2))
