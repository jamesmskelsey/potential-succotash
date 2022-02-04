#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value = None):
    # figure out how many items to add
    items_to_add = min_size - len(array) if min_size > len(array) else 0
    # creates an array of length items_to_add filled with value and extends array with the result
    array.extend([value for x in range(items_to_add)])
    return array