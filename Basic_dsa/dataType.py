# In Python, the data type is set when you assign a value to a variable:
# Variables can store data of different data types and different types can do different things.
# Built In data Types ;

# str ,int ,float,complex,list,tuple,range,dict,set,frozenset,bool,byte,bytearray,memoryview,NoeType;

a = 5
print(type(a))                       # int

b= "Hello How are you today?"
print(type(b))                       # str

c=20.5    
print(type(c))                       # float

d= 1j
print(type(d))                       # complex

e = ["apple","banana","cherry"]
print(type(e))                       # list

f = range(6)
print(type(f))                       # range

g = {"name":"rohit","age":35}
print(type(g))                       # dict

h=("apple","banana","mango")
print(type(h))                       #tuple

i = {"a","b","c","d"}
print(type(i))                       #set

j = ({"apple","banana","cherry"})
print(type(j))                       #frozenset

k = True
print(type(k))                       #bool

l=b"hello"
print(type(l))                       #bytes
print(l)

m=bytearray(5)  
print(type(m))                       #bytearray
print(m)

n=None
print(type(n))                       #NoneType

# We can set the specific dataType by constructor functions:

z= str("Hello folks")
print(type(z))

dictionary = dict(name="Ravi",age=25)
print(type(dictionary))
print(dictionary)

