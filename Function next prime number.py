def nextprime(a,b):
       for x in range(a,b):
              for num in range(2,x):
                     if(x%num==0):
                            break   
              else:
                     print(x)
                     break              
       
     
p=int(input("Enter the no to find the next prime number:"))
q=100
nextprime(p,q)
