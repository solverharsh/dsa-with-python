#Print the multiplication table for a given number up to 10 but , skip the fifth iteration;

num = int(input("Enter the number : "))

for i in range(1,11):
    if i ==5:
        continue
    # print(num , 'x' , i , num*i) 
    print(f"{num} x {i} = {num*i}")

    # ------OUTPUT-------#

# Enter the number : 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50