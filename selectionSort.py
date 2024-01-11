# Selection sort Algorithm :

def selectionSort(arr):
  n=len(arr)
  for iter_num in range(n):
    min_index=iter_num
    for curr in range(iter_num+1,n):
      if arr[curr]<arr[min_index]:
        min_index=curr
    arr[min_index],arr[iter_num] = arr[iter_num],arr[min_index]

arr = [12,14,7,6,4,1,3]
selectionSort(arr)
print(arr)

