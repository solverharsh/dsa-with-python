# int ,float,cmoplex ;

x= 1                #int
y=2.8               #float
z=0+5j              #complex
m = -3255522

# To verify the type of any object in Python, use the type() function

print(type(x))
print(type(y))
print(type(z))
print(type(m))

#OUTPUT:
# <class 'int'>
# <class 'float'>  
# <class 'complex'>
# <class 'int'>

# Float can also be scientific numbers with an "e" to indicate the power of 10.
value =2e2 # 2*pow(10,2)
print(value)

# convert from one Type to another;

a = 1
b = 3.5
c = 1+6j

p = float(a)
print(p,type(p))

q = int(b)
print(q,type(q))

r = complex(a)
print(r,type(r))

# 1.0 <class 'float'>
# 3 <class 'int'>
# (1+0j) <class 'complex'>

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1,10))

