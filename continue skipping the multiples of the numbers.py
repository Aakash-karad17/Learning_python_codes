n=int(input("enter the range of number: "))
z=int(input("enter you which want to skip multiple of number: "))

for x in range(1,n):
     if(x%z==0):
        continue
     print(x)  # not in if loop
     x=x+1

