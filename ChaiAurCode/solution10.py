# Given a string , find the first non -repeated character ;

str = 'aaaaabcccc'

for char in str:
    if str.count(char)==1:
        print(char)
        break

str1 = 'teet'

for char in str1:
    if str1.count(char)==1:
        print(char)
        break