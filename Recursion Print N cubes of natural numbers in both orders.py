def sqre(n):
        
        if(n>0):
             sqre(n-1)
             print(n**3)
x=int(input("Enter the number:"))
print("\nThe cube of N natural numbers are:")
sqre(x)

def revsqre(p):


       if(p>0):
               print(p**3)
               revsqre(p-1)

        
y=int(input("Enter the range of numbers to print squares in reverse order:"))
print("\nThe cube of natural numbers in reverse order is:")
revsqre(y)
