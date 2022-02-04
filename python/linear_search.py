array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
  output = None
  for i, el in enumerate(array_to_search_through):
    if el == value_to_find:
      output = i
      break
  return output

def linear_search_global(value_to_find, array_to_search_through):
    return [idx for idx, el in enumerate(array_to_search_through) if el == value_to_find]

print(linear_search(24, [11,12,3,2]))
print(linear_search_global('d', list('bananas')))
print(linear_search_global('b', list('bananas')))
print(linear_search_global('a', list('bananas')))