
#EVEN NUMBER GAME


c=1

while(c<=3):
    x=int(input("enter the even number:"))
    if(x%2==0):
        break
    c+=1
if(c==4):
    print("you lose")
else:
    print("you win")

# ODD NUMBER GAME

ca=1

while(ca<=3):
    y=int(input("enter the odd number to win:"))
    if(y%2==0):
        pass
    else:
        break
    ca+=1
    
if(ca==4):
    print("you lose")
else:
    print("you win")
