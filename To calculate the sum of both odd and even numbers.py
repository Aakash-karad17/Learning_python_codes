n=int(input("enter the number if you want to find odd between (1 to 10 type 9) : "))
""" both odd and even number calculated by this method"""
x=1
s=0
if(n==0):
 print("none!")
while(x<=n):
    s=s+n
    n=n-2
    print(s)


