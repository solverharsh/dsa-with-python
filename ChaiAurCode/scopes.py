# Learning about scopes and Closure ;
username = "Vipin"      # global

def func():
    username = "Amit"   # Local
    print(username)

print(username)
func()

x = 99
def func2(y):
    z = x + y
    return z
result = func2(1)
print(result)

def func3():
    global x           # local variable can be made global to access it outside;
    x = 12

func3()
print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()
# f1()


# Example  of closure :

def f1():
    x = 80
    def f2():
        print(x)
    return f2
res = f1()
res()

# Examples of Closure :

def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f =chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))
