x=int(input("enter the value of month to calculate the no.of days in months: "))
y=int(input("entr the value of year: "))
if(x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12): 
  print("The number of days is 31")
elif((x==2) and ((y%4==0))):
  print("the number of days is 29")
elif(x==2):
 print("the number of days is 28")
else:
  print("the number of days is 30")
    
    
