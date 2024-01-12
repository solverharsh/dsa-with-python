# Python Lambda :
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x= lambda a : a+100
print(x(50))
# 150

y = lambda a,b:a*b
print(y(5,5))
# 25

z= lambda a,b,c:a+b+c
print(z(10,10,10))
# 30

def double(n):
  return lambda a:a*n

res = double(2)
print(res(150))
# 300

def poweroftwo(n):
  return lambda a :a**n

result = poweroftwo(2)
print(result(8))
# 64
