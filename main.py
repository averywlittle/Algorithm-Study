# This file is reused as driver space to test programs and solutions

import PA_3

content_array = []

with open('test_data/quick_sort.txt') as f:
  for line in f:
    content_array.append(int(line.rstrip()))

count = PA_3.quick_sort(content_array, 0, len(content_array)-1)
print(content_array)
print('count', count)
