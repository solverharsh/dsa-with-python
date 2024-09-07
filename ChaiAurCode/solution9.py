# Reverse a String using a loop :

str = "ChaiAurCode"
# rev_str = str[::-1]
# print(rev_str)

rev_str = ""
for i in str:
    rev_str = i + rev_str
print(rev_str)
print(str)