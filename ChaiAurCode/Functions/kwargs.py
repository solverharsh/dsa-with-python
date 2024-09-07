# Create a function that accepts any number of keyword argumnets and prints them in the format key : value .

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name = 'Roman')
print_kwargs(name = 'shaktiman' , power ='lazer')
print_kwargs(name = 'shaktiman' , power ='lazer',enemy = 'Cena')