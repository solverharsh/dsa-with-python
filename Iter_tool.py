my_tuple = ("apple" , "banana" , "cherry")

I = my_tuple.__iter__()
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

# I = iter(my_tuple)
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))

#---------------OUTPUT--------------------------#

# apple
# banana
# cherry
# Traceback (most recent call last):
#   File "/workspaces/dsa-with-python/Iter_tool.py", line 6, in <module>
#     print(next(I))
#           ^^^^^^^
# StopIteration

my_list = [1,2,3,4,5]

I = iter(my_list)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))

#------------------------OUTPUT---------------------------#
# 1
# 2
# 3
# 4
# 5
# Traceback (most recent call last):
#   File "/workspaces/dsa-with-python/Iter_tool.py", line 32, in <module>
#     print(next(I))
#           ^^^^^^^
# StopIteration