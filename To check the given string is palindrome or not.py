n=input("enter the number: ")

reverse=n[len(n)::-1]


print("The reverse string is:",reverse)

if(reverse==n):
        print("The given string is palindrome")
else:
        print("not palindrome")
