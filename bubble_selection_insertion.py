
def bubble(arr):
  n = len(arr)
  for iter_num in range(n):
    for curr in range(n-1-iter_num):
      if(arr[curr]>arr[curr+1]):
        # temp=arr[curr]
        # arr[curr]=arr[curr+1]
        # arr[curr+1]=temp
        arr[curr],arr[curr+1]=arr[curr+1],arr[curr]

def selectionSort(arr):
  n=len(arr)
  for iter_num in range(n):
    min_index=iter_num
    for curr in range(iter_num+1,n):
      if arr[curr]<arr[min_index]:
        min_index=curr
    arr[min_index],arr[iter_num] = arr[iter_num],arr[min_index]

def insertion(arr):
  n=len(arr)
  for wall in range(1,n):
    curr = arr[wall]
    pos_ptr =wall-1
    while pos_ptr>=0 and curr<arr[pos_ptr]:
      arr[pos_ptr+1]=arr[pos_ptr]
      pos_ptr-=1
    arr[pos_ptr+1]=curr

arr = [12,14,7,6,4,1,3]
# bubble(arr)
# selectionSort(arr)
insertion(arr)
print(arr)