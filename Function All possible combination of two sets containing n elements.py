def sets_withlist(a):

       n=len(a)

       for i in range(1,n+1):
             for j in range(1,n+1):
                 print("{",i,",",j,"}",end=",")
x=eval(input("enter a set:"))
sets_withlist(x)
