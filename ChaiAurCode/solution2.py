 # movie ickets are priced based on the age  : $12 for adults(18 and over) ,$ 8for children . Everyone gets a discount on Wednesday.

age = int(input("Enter your age: "))
day = input("Enter the weekday :")
dow = day.lower()

price=12 if age>=18 else 8

if dow=='wednesday':
    if age<18:
        price = price-2
    else:
        price = price-2

else:
    if age<18:
        price = 8
    else: 
        price = 12

print (price)

#                                                   OUTPUT:
# @solverharsh ➜ /workspaces/dsa-with-python/ChaiAurCode (main) $ python assignment2.py
# Enter your age: 10
# Enter the weekday :wednesday
# 6
# @solverharsh ➜ /workspaces/dsa-with-python/ChaiAurCode (main) $ python assignment2.py
# Enter your age: 35
# Enter the weekday :Tuesday
# 12