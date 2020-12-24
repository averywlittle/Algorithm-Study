def find_median(arr, left, right):
  median = (right + left) // 2

  median_of_three_arr = sorted([arr[left], arr[median], arr[right]])

  if median_of_three_arr[1] == arr[median]: return median
  elif median_of_three_arr[1] == arr[left]: return left
  else: return right

"""
rearrange array so left of pivot is less than pivot and right of pivot is greater than pivot. do this in place. keep track of two boundaries. j: between what we've 
seen and what we haven't. i: where the pivot logically falls
"""
def partition(arr, left, right):
  # swap last element
  ''' last_temp = arr[right]
  arr[right] = arr[left]
  arr[left] = last_temp '''
  
  # rule of three implementation
  median = find_median(arr, left, right)

  # don't need to swap if left is median
  if median != left:
    last_temp = arr[median]
    arr[median] = arr[left]
    arr[left] = last_temp 
 

  pivot = arr[left]
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
def quick_sort(arr, left, right):
  if left >= right: return 0

  pivot = partition(arr, left, right)

  left_count = quick_sort(arr, left, pivot-1)
  right_count = quick_sort(arr, pivot+1, right)

  return (left_count + right_count + (right - left))
  
"""
When there is a recursive call on a subarray of length m, add m - 1
to the running total of comparisons. Finally, return the number of comparisons.
"""