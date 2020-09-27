def func(n):
        if(n>0):
          func(n-1)
          print(n)

x=eval(input("Enter the number:"))
func(x)

