print("*****NUMBER SYSTEM*****\n")
print("In python language it always gives decimal representation\n")
x=45
print(x) # which is decimal representation
x=0b101  # This is binary representaton
print(x) # but this also gives decimal representation
y=0o42   # this is octal representation
print(y) # but this also gives decima representation
z=0x3f   # this is hexdecimal representation
print(z) # but this gives decimal representation

print("\n\nIn order to print the value of x that is 0b101,0o42,ox3f are the representation of numbers system we use built functions\n\n")

print(bin(x))
print(oct(y))
print(hex(z))


print("\n\n In order to use slicing which means 101,42,3f\n\n")


print(bin(x)[2::])
print(oct(y)[2::])
print(hex(z)[2::])

