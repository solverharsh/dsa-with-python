# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = int(1)
y= int(3.9)
z=int("5")

print(x,y,z) # 1 3 5

a = float(3)
b = float(4.0)
c = float("10")

print(a,b,c)  # 3.0 4.0 10.0

l= str(2)
m= str(2.1)
n= str("2")
print(l,m,n)