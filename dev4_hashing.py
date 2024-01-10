# Creating a set :
myset = {"apple","banana","cherry"}
print(myset)
# {'apple', 'banana', 'cherry'}

# Duplicate values will be ignored :
thisset = {1,2,3,1,2,3}
print(thisset)
# {1, 2, 3}

# True and 1 is considered the same value:
newSet = {"apple", "banana", "cherry", True, 1, 2}
print(newSet)
# {True, 2, 'banana', 'cherry', 'apple'}

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
# {False, True, 'banana', 'apple', 'cherry'}

print("Length of newSet is : ",len(newSet))
print(type(thisset))

thisset.add("orange")

# Access items of set ;
# for x in thisset :
#   print(x)

l = [1,2,3,4,5]
thisset.update(l)
print(thisset)
thisset.remove("banana")
print(thisset)

thisset.clear()
print(thisset)     # set()

del thisset
# print(thisset)
# NameError: name 'thisset' is not defined

s= {1,2,3,4,5}
l=[8,9,10]
s.update(l)
print(s)

set1= {"a","b","c"}
set2={11,12,13}
set3= set1.union(set2)
print(set3)
# {13, 'a', 'c', 11, 12, 'b'}

# Dictonaries :

thisDict = {"brand":"ford","model":"Mustang","year":"1964"}
print(thisDict)
print(type(thisDict))

d ={}
print(type(d))        #<class 'dict'>

print(thisDict["brand"])
print(thisDict.get("model"))
print(thisDict.keys())
thisDict["year"] =2021
print(thisDict["year"])
print(thisDict.values())
print(thisDict.items())

#USing dict() Constructor:

new_dict = dict(name="Rohit",age=32,country="India")
print(new_dict)
# {'name': 'Rohit', 'age': 32, 'country': 'India'}

# Dictionary Methods :
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


