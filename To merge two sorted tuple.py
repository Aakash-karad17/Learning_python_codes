a=eval(input("enter th First tuple tuple:"))


b=eval(input("enter a Second tuple"))


q=tuple(sorted(a))
w=tuple(sorted(b))



z=q+w
p=tuple(sorted(z))

print("the merged sorted tuple is",p)
print(type(q))
print(type(w))
print(type(a))
print(type(b))
print(type(z))
