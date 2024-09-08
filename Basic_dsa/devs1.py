x = 5
print(x)        #5

x,y,z = 7,4,6
print(x,y,z)    # 7 4 6

a=b=c=10
print(a,b,c)    # 10 10 10

print(id(a))
print(id(b))
print(id(c))
# same location in memory as the values are same
# 140708755880664
# 140708755880664
# 140708755880664

m =6
n=m
print(id(m))
print(id(n))
# 140708755880536
# 140708755880536

text = "what" +" "+'is'+" "+"python ?"
print(text)
# Interesting stuffs below :
newText = 3*"well..."
print(newText)
print(type(newText))

word = "India"
print(word[1])
print(word[-1])
print(len(word))
print(word[0:3])        #Ind as default step is 1
print(word[0:3:2])      #Id as step here is 2 so it will skip 1 character in between;
print(word[3:0:-1]) 

num= '0123456789'
print(num[1:8])        # last index is not included (1234567);
print(num[8:0:-1])     # starting from the back (87654321);  
print(num[1:9:2])      # here step is 2  (1357);
print(num[9:0:-2])     # (97531);
print(num[:9])         # (012345678);
print(num[0:])         #(0123456789);

file1 = "This is India"
file2 = "We love our country"
print(file1,file2,sep="&&")

l1 =["mango","apple","banana","papaya"]
for x in l1:
  print(x,end=" ")    # mango apple banana papaya
  # print(x)
# mango
# apple
# banana
# papaya
  
print(type(l1))       # <class 'list'>

