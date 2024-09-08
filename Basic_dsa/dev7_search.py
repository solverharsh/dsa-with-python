# print("Welcome to learning the search algoithm in DSA !!")

# Linear search :

arr = [1,6,4,8,9,5,10,11,15,18]
key = int(input())
found = False
for x in arr:
  if x ==key:
    found=True
    print("found !!")

if found==False:
  print("Not found !!")

# Binary Search : O(log n)
arr = [1,6,4,8,9,5,10,11,15,18]
arr.sort()
print(arr)
key= int(input())
found=False
first =0
last =len(arr)-1
# for i in range(len(arr)):
while(first<=last):
  mid = (first+last)//2
  if arr[mid]==key:
    found =True
    print("The key is present at",mid," position")
    break
  elif arr[mid]<key:
    first=mid+1
  else :
    last=mid-1

if found==False:
  print("Key is Not Found!!")

# find the first occurence of any element if the duplicates are also present :
# arr = [1,5,4,8,9,5,10,11,15,5]

def binarySearch(arr,target):
  low =0
  high=len(arr)-1
  ans=-1

  while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
      ans=mid
      high=mid-1
    elif arr[mid]<target:
      low=mid+1
    else:
      high=mid-1   
  return ans
 

# arr = [5,5,5,5,5,5,5,5,5,5,5]
arr = [1,5,4,8,9,5,10,11,15,5]
output=binarySearch(arr,5)
print(output)

  




