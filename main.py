import PA_2

content_array = []

with open('test_integer_array.txt') as f:
  for line in f:
    content_array.append(int(line.rstrip()))
  print(content_array)

z = PA_2.sort_and_count_inversions(content_array)

print('array', z)
#print(inversions)