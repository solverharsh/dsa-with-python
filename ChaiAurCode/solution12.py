# Keep asking the user for input until they enter a number between 1 and 100;

while True:
    number = int(input("Enter value between 1 and 10 : "))
    if 1<=number<=10:
        print("number between 1 and 10 found , Thanks!!")
        break
    else:
        print("Invalid number , please try again !!")