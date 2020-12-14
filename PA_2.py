"""
Compute the number of inversions in the input array
An inversion is defined as a pair of array indices i and j where i < j and
arr[i] > arr[j]
A sorted array has 0 inversions
Left inversion if i, j <= n/2
Right inversion if i, j > n/2
Split inversion if i<= n/2 > j
"""
def sort_and_count_inversions(arr):

  # base case
  if len(arr)<=1:
    return arr, 0
  
  mid = len(arr) // 2
  left, left_inv = sort_and_count_inversions(arr[:mid])
  right, right_inv = sort_and_count_inversions(arr[mid:])
  # count left and right inversions and pass to the final merge
  inv = left_inv + right_inv

  return merge_and_count_split(left, right, inv)

""" 
Augment a merge sort approach so that when an item from the second sub array
is processed ahead of x remaining items in the first sub array, add x to the total
count of split inversions
All inversions will be categorized as 'split inversions'
This should run in O(n)
"""
def merge_and_count_split(left, right, inv):

  result = []
  left_index, right_index = 0, 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      #increment total inversions by number of elements remaining in left
      inv += (len(left) - left_index)
      right_index += 1

  # append the remaining tail of the arrays
  result += left[left_index:]
  result += right[right_index:]
  # return the sorted result array and the total inversions
  return result, inv

# brute force nested loop approach
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count