#List Comprehension :

l = [1,2,3,4,5,6]
l1 = [x**2 for x in l ]
print(l1)

l2 = [x**3 for x in l if x%2==0]
print(l2)

l3 = [x**3 if x%2==0 else x**2 for x in l]
print(l3)

l4 = [x for x in range(10)]
print(l4)
l5 = [x for x in range(1,11)]
print(l5)

thislist = [10,5,6,7,3,2,6]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# Tuple : Immutable
a = (1,2,3,4,5)
print(type(a))
print(id(a))

# a[-1].append([7,8,9])
# print(a)
# print(id(a))

b = (1)       
print(type(b))      #<class 'int'>

c = (1,)
print(type(c))      #<class 'tuple'>

# Functions :
# if __name__=__main__:

def func(a,b):
  if a%2==0:
    return b
  return b**2
x= func(2,3)   # 3
y=func(3,3)    # 9
print(x,y)     # 3  9

def f1(a,b,c):
  print(a,b,c)

def f2(x,y,z):
  print(x,y,z) 

f1(2,3,4)
f2(z=6,x=7,y=8)

a = 10

def fun():
  print(a)
  y=a+7       # this is modification not changing the actual variabe of a variable ,value can be changed but reference can't be changed;
  # a=7           # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value  ; 
  print(y)

fun() 
print(a) 

p =11 

def func():
  global p        # Reference can be changed by calling the global  variable
  p=5
  print(p)

func()
print(p)

# In Built Function:

text = "Welcome to learning python"
newText=text.split(" ")
print(newText)
newText = " ".join(newText)
print(newText)

# map(int,["1",2.33,True])
# x= list(map(int,l.split()))
# print(x)

# x= [x for x in l]
# print(x)

# x= list(map(int,input().split()))
# print(x)

# m= [1,2,3,4,5]
x= list(map(int,input().split()))
print(x)

# OUTPUT:- [1, 2, 3, 4]
