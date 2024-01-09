num = int(input())
print("wow"*num)

text = input()
print(text)

# list :
car = ["honda","maruti","BMW"]
print(car)
car.append(10)
print(car)
print(car[-1])
car.append(True)
print(car)
car.append([1,2,3,4,5])
print(car)
print(car[-1][2]) 

# if elif else ;
x = int(input())
if(x==1):
  print("Hello")
elif(x==2):
  print("Bye")
elif(x==3):
  print("Welcome")
else :
  print("?")

burger = True
coke= True
print("Enter the age: ")
age = int(input())
cost=0

if burger:
  cost+=170
if coke:
  cost+=50
if age<9:
  cost=int(cost*0.8)
elif age>59:
  cost = int(cost*0.7)

print("pay",cost,"rupees")

a = True
b =True
print(a and b)
print(a or b)
print( not a )
print(not(a and b))
print(not(a or b))

# Loop :
# while loop and for loop

m = 5

while(m>0):
  print(m)
  m-=1
print("Understood the concept of whie loop")

arr =[1,2,3,4,5]

# for x in arr:
#   print(x)

for i in range(len(arr)):
  print(arr[i])

print("Understood the for loop in Python")

for i in range(10):    #It means range(0,10,1)
  print(i)

for i in range(3,19,2):
  print(i)

print(sum(arr)) # direct method to find the sum of iterables
# BAsic approach using for loop;
sum = 0
for x in arr :
  sum+=x
print(sum)

sum=0
for i in range(len(arr)):
  if(i%2==0):
    sum+=arr[i]
print("Sum of even index values is :",sum)
 




