"""
rearrange array so left of pivot is less than pivot and right of pivot is greater than pivot. do this in place. keep track of two boundaries. j: between what we've 
seen and what we haven't. i: where the pivot logically falls
"""
def partition(arr, left, right):
  pivot = arr[right]
  i = left + 1
  j = left + 1
  for j in range(j, right + 1):
    if arr[j] < pivot:
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp
      i = i + 1

  temp = arr[left]
  arr[left] = arr[i - 1]
  arr[i - 1] = temp
  return i - 1

# quick sort
def quick_sort(arr, left, right, count):
  if left >= right: return

  count += (right - left)
  pivot = partition(arr, left, right)

  quick_sort(arr, left, pivot-1, count)
  quick_sort(arr, pivot+1, right, count)

  return count



  
"""
When there is a recursive call on a subarray of length m, add m - 1
to the running total of comparisons. Finally, return the number of comparisons.
"""