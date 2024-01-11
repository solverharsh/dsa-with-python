# Sorting Algorithm 

def bubble(arr):
  n = len(arr)
  for iter_num in range(n):
    for curr in range(n-1-iter_num):
      if(arr[curr]>arr[curr+1]):
        # temp=arr[curr]
        # arr[curr]=arr[curr+1]
        # arr[curr+1]=temp
        arr[curr],arr[curr+1]=arr[curr+1],arr[curr]

arr = [12,5,8,2,9,15,90]
bubble(arr)
print(arr)


