import PA_2

content_array = []

with open('integer_array.txt') as f:
  for line in f:
    content_array.append(int(line.rstrip()))

arr, inv = PA_2.sort_and_count_inversions(content_array)

print('length content', len(content_array))
print('length result', len(arr))
print('inversions', inv)