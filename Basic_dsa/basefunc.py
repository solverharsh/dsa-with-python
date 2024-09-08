# binary : 0,1
# Octal  : 0,1,2,3,4,5,6
# Hexadcimal : 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f

binary = bin(12)
print(binary)           #0b1100

two = hex(12)
print(two)              #0xc

three = int("1100",2)
print(three)

four = int("1100",3)
print(four)

five = int("1111",2)
print(five)

six = ord('a')
print(six)

seven = ord("\n")
print(seven)

# eight = chr(10)
# print(eight)

#Undertanding f string
first = "hello"
second = "welcome"
print(f"{first} {second} to learning Python ")
print(first,second,sep="#",end="$$")
print(".")
# hello welcome to learning Python
# hello#welcome$$

def f(a,b,c):
  return a+b+c

s=f(1,2,3)
print(f"The sum is {s}")

# sum=0
def f(*x):
  return (x[2],x[3],x[5])

res = f(1,2,3,4,5,6)
print(res)
# (1, 2, 3, 4, 5, 6)

def func(a,b,*args,**kwargs):
  print(f"{a}{b}{args}{kwargs}")

func(5,6,7,8,9,2,e=10,f=16,l=20)

# 56(7, 8, 9, 2){'e': 10, 'f': 16, 'l': 20}

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

