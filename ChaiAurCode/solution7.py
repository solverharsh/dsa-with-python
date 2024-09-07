# Calculate the sum of even numbers upto a given number n ;
n =int(input("Enter the value of n : "))
sum_even = 0
for num in range(1 , n+1):
    if num%2 == 0:
        sum_even+=num
print(f"Sum of even numbers till n is : {sum_even}")

# n =11  
# 2+4+6+8+10 = 30 