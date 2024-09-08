# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# text = "Welcome to this beautiful planet Earth !!"
text = 'Welcome to this beautiful planet Earth !!'
print(text)

# Multiline Strings :
# You can assign a multiline string to a variable by using three quotes:

# newText = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""

newText = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(newText)

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Accessing the character at specific position below :
txt = "Python is love"
print(txt[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for i in txt :
  print(i)

# To get the length of a string, use the len() function.Space is also counted.
  
print(len(txt))

# Check String :
# To check if a certain phrase or character is present in a string, we can use the keyword in.

newTxt = "The best things in life are free!"
print("free" in newTxt)

if "free" in newTxt :
  print("Yes free is present")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
newTxt = "The best things in life are free!"
print("love" not in newTxt)

if "love" not in newTxt :
  print("love is not present in the text")

# Slicing :
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
  
print(newTxt[0:7])  #The bes
# Get the characters from the start to position 7 (not included):
print(newTxt[:7])   #The bes
# By leaving out the end index, the range will go to the end:
print(newTxt[0:])   #The best things in life are free!

word = "    DataStructure    "
print(word.upper())
print(word.lower())

# The strip() method removes any whitespace from the beginning or the end:
print(word.strip()) 

# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

firstName = "Virat"
lastName = "Kohli"
print(firstName+" "+lastName)

# Python - Format - Strings :
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

age =37
place= "Mumbai"
about = "I am professional cricketer and my age is {0} and my birthplace is {1}"
print(about.format(age,place))

# Python - Escape Characters
# An escape character is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."

# Python - String Methods :
"""Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	Description :
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""
