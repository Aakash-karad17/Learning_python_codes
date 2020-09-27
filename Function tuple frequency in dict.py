"""t=eval(input("Enter a tupple"))


q=0
for x in t:
    if(t.index(x)==q):
        print(x,"-",t.count(x))
    q=q+1


print("\nThe frequency of tuple in the dict is:\n")
d1={y : t.count(y)   for  y in t}
print(d1)
"""
def freq(t):
    d={}
    for z in t:
         d[z]=t.count(z)
    
    print(d)


x=eval(input("Enter the tuple to find its frequency of elements:"))

freq(x)

    


