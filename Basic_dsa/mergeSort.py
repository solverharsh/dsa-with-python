# Merge Sort Algorithm: O(nlogn)

def mergeSort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    mergeSort(left)
    mergeSort(right)

    leftptr=rightptr=arrptr = 0
    while(leftptr<len(left) and rightptr<len(right)):
      if left[leftptr]<right[rightptr]:
        arr[arrptr]=left[leftptr]
        leftptr+=1
      else:
        # if left[leftptr]>right[rightptr]:
        arr[arrptr]=right[rightptr]
        rightptr+=1
      arrptr+=1

    while leftptr<len(left):
      arr[arrptr]=left[leftptr]
      leftptr+=1
      arrptr+=1

    while rightptr<len(right):
      arr[arrptr]=right[rightptr]
      rightptr+=1
      arrptr+=1

# arr = [12,14,7,6,4,1,3]
arr = [20,1,4,7,9,4,2,6,8,1,100]
mergeSort(arr)
print(arr)


  