def even(list1):

           s=0
           s1=0
           print("\n")
           for x in list1:
                  if(x%2==0):
                        print("The even numbers are:",x)
                        s=s+x
           print("\n The sum of even numbers are:",s)
           for y in list1:
                  if(y%2!=0):
                        print("The odd numbers are :",y)
                        s1=s1+y
           print("\n The sum of odd numbers are:",s1)


i=eval(input("Enter a list:"))
even(i)

                          
                             
                             
                             
