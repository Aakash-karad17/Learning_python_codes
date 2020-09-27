def func(a):
        d={x[0:1:] : x for x in a}
        print(d)

x=eval(input("Enter the list of strings:"))

func(x)
