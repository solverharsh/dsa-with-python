# check if all the elements in a list are unique . If a duplicate is found , exit the loop and print the duplicate;

items = ['apple','banana','orange','apple','mango']
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item : " , item)
        break
    unique_item.add(item)