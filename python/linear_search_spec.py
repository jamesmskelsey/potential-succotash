from linear_search import linear_search, linear_search_global

print(linear_search(3, [1,2,3]) == 2)
print(linear_search(4, [1,2,3]) == None)
print(linear_search(13, [1,2,3]) == None)

print(linear_search_global('d', list('bananas')) == [])
print(linear_search_global('b', list('bananas')) == [0])
print(linear_search_global('a', list('bananas')) == [1,3,5])
