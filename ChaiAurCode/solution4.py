pass_length = int(input("Enter password length : "))

if pass_length<6:
    print("weak")
elif pass_length<=10:
    print("Medium")
else:
    print("Strong")

