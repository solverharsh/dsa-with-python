# prime number checker ;

num = int(input("Enter the number : "))

is_prime = True

if num >1:
    for i in range(2,num):
        if (num%i)  == 0:
            is_prime = False
            break

if is_prime ==False:
    print("The number is not prime")
else:
    print("THe number is prime")