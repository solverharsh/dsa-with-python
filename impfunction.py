# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
# zip(iterator1, iterator2, iterator3 ...)
# iterable1, iterable2, iterable3 ...	Iterable objects that will be joined together

a = [1,2,3,4,5]
b = [0,9,8,7,6,5,4,3,2,1]

z=zip(a,b)
print(z)        # <zip object at 0x000001A87179C040>
res=list(z)     #convert the zip to list
print(res)
# [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6)] creates tuple fromelements of both the list till the element of one list get finished.

# Python enumerate() Function:

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
# <enumerate object at 0x0000017E40663330>
print(list(y))
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

for i,el in enumerate(b):
  print(i,el)

# 0 0
# 2 8
# 3 7
# 4 6
# 5 5
# 6 4
# 7 3
# 8 2
# 9 1
  
for x in enumerate(b):
  print(x) 

# (0, 0)
# (1, 9)
# (2, 8)
# (3, 7)
# (4, 6)
# (5, 5)
# (6, 4)
# (7, 3)
# (8, 2)
# (9, 1)
  
output = list(enumerate(b))
print(output)

# [(0, 0), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]

