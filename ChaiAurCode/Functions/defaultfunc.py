# Write a function that greets user . If no name is provided  , it should greet with a default value ; 

def greet(name = "Harsh"):
    return f"Hello, {name} !!"

result = greet("Amit")
result = greet()
print(result)