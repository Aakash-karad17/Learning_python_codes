def prime(n):

     list1=[]
     for i in range(2,n+1):
          for num in range(2,i):
               if(i%num==0):
                    break
          else:
               print("The prime numbers are:",i)
q=int(input("enter the range:")) 

prime(q)

