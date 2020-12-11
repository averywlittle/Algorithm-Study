

def add(x, y):
  print(x + y)

def count_inversions(arr, n):

  # base case
  if n==1:
    return 0
  else:
    x = count_inversions(arr, n/2)
    y = count_inversions(arr, n/2)
    z = count_split(arr, n)

""" 
Augment a merge sort approach so that when an item from the second sub array
is processed ahead of x remaining items in the first sub array, add x to the total
count of split inversions
"""
def count_split(arr, n):

  if n==1:
    return 0

  
def closest_pairs(arr, n):
  return 0

def closest_split_pair(arr, n):
  return 0