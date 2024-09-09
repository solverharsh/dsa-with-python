try:
    a = 6
    b = 0
    c = a/b
    print(c)
except Exception as e:
    print(e)

finally:
    print("This will execute always..!!")


print("Hello World")

# division by zero
# Hello World


try:
    l = [10,20,30,40,50]
    l[10]

except Exception as e:
    print(e)

else:
    print("It will execute only when try block will exceute successfully !!")

finally:
    print("This will execute always..!!")
# list index out of range

try:
    dict = {
        "name":"harsh",
        "age" :23,
        "email" :"abc@gmail.com",
        "address":"pariward sadan"
        }
    dict["phone"]

except KeyError as e:
    print(e)

else:
    print("It will execute only when try block will exceute successfully !!")

finally:
    print("This will execute always..!!")