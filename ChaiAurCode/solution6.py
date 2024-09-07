# Given list of numbers , count how many are +ve;

numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
count = 0
for i in numbers:
    if i > 0:
        count+=1
print(f"The count of +ve integers are: {count}")