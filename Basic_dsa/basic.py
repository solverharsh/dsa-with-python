# UNDERSTANDING PYTHON : 

# It is used for:
# web development (server-side),
# software development,
# mathematics,
# system scripting.

# Why Python?

# Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
# Python has a simple syntax similar to the English language.
# Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
# Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
# Python can be treated in a procedural way, an object-oriented way or a functional way.

print("Hello Welcome to Python")

# Python Indentation :

# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

if 5>2:
  print("Five is greater than two")

# Python will give you an error if you skip the indentation:
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# Python Variables :
  
num =5
print("The number is ", num)

# String variables can be declared either by using single or double quotes:
# name = "Rohit Sharma"
name = 'Rohit Sharma'
print(name)

# Note :
# Python does not really have a syntax for multiline comments.
# To add a multiline comment you could insert a # for each line:
# Or, not quite as intended, you can use a multiline string.

# Note :
# Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
"""
This is a comment
written in
more than just one line
"""
# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 5
print("The value of x is : ", x)

x = "hello now x contins string !!"
print(x)

# If you want to specify the data tye of a variable,this can be done with casting;

a = str(3)
print("Value of a is : ", a)

b = int(5)
print("Value of b is :", b)

c = float(3.33)
print("Value of c is :", c)


# OUTPUT :
# Hello Welcome to Python
# Five is greater than two     
# The number is  5
# Rohit Sharma
# The value of x is :  5       
# hello now x contins string !!
# Value of a is :  3
# Value of b is : 5
# Value of c is : 3.33

# You can get the data type of a variable with the type() function.

print(type(a))
print(type(b))
print(type(c))

# OUTPUT :
# <class 'str'>
# <class 'int'>
# <class 'float'>

# Remember that variable names are case-sensitive

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:
myVariableName = "John" # Camel Case
MyVariableName = "John" # Pascal Case
my_variable_name = "John" # Snake Case

# Python allows you to assign values to multiple variables in one line;
# Note: Make sure the number of variables matches the number of values, or else you will get an error.

m , n , o = 1,2,3
# print(m)
# print(n)
# print(o)

print(m,n,o)

# And you can assign the same value to multiple variables in one line:

p=q=r=5
# print(p)
# print(q)
# print(r)
print(p,q,r)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called " unpacking ".

fruits = ["apple", "banana" , "orange" , "grapes"]

e,f,g,h =fruits

# print(e)
# print(f)
# print(g)
# print(h)

print(e,f,g,h)

firstName = "Virat "
lastName = "Kohli"

# Another method of printing output;
print(firstName + lastName)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types.

# Global Variable

text = "fun"

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

def myfunc():
  text = "awesome"
  print("Learning Python is" ,text)

myfunc()

print("Learning Python is",text)

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def newFunc(): 
  global newText 
  newText = "best"
  print("Pyhton is",newText) 
 
newFunc()

print("I am",newText)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)