# Compute the factorial of number using for loop && whille loop ;

# 5! = 5*4*3*2*1

num = int(input("Enter the number : "))
fact = 1

# for i in range(2 , num+1):
#     fact*=i
# print(f"The factorial of given number is {fact}")

while num>0:
    fact*=num
    num-=1
print(f"The factorial of given number is {fact}")