# User Input :
# Python allows for user input.

# Python 3.6 uses the input() method.

username = input("Enter username: ")
print(f"username is {username}")

number = input("Enter the number: ")
print(f"The number is {number}")

# Python Try Except :

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
try:
  print(x)
except:
  print("An error occured")
# # An error occured

x=5
try:
  print(x)
except:
  print("An error occured")
  
# Many Exceptions:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# Variable x is not defined
  
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
# Hello
# Nothing went wrong
  
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
  
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# Something went wrong
# The 'try except' is finished
  
try:
  f=open(demo.txt)
  try:
    f.write("writing content")
  except:
    print("something went wrong while writing in demo file")
  finally:
    f.close()
except:
  print("something went wrong while opening the file")
# something went wrong while opening the file
  
# Raise an exception:
  
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
  
x = -1

if x<0:
  raise Exception("no number below zero")
Exception: no number below zero

# Raise a TypeError if x is not an integer:

x = "Python"

if not type(x) is int:
  raise Exception("typeerror only integer are allowed")

# raise Exception("typeerror only integer are allowed")
# Exception: typeerror only integer are allowed