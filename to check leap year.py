x=int(input("Enter the year to check leap year or not:"))
if x%4==0:
    print("%d This year is a Leap year" %x)
elif x%100==0:
    print("%d this year is a Leap year" %x)
elif x%400==0:
    print("%d this year is a Leap year" %x)
else:
    print("%d This is not a Leap year" %x)
