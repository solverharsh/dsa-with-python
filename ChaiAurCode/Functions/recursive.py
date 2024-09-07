# Problem : Create a recursive function to calculate the factorial of number :

def fact (num):
    if num == 1 or num==0:
        return 1
    return num * fact(num-1)

result = fact(5)
print(result)

# factorial(5)
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))
# = 5 * (4 * (3 * (2 * 1)))
# = 120