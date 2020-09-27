
def toh(n,sour,des,aux):
   if n==1:
      print("\ndisk move from",sour,"to",des)

   else:
      print(n-1,sour,aux,des)
      print("\nDisk move from",sour,"to",des)
      toh(n-1,aux,des,sour)
n=int(input("\nEnter the number of disk:"))
toh(n,"A","C","B")

print("\nEnd")

