import math


def binary_search(target, array, start_index=0, end_index=0):
    if end_index == 0:
        # that means we just started, need to move to the end of the array
        end_index = len(array) - 1

    # divide the length, find a middle index
    check_index = end_index - math.ceil((end_index - start_index) / 2)
    # short circuits...
    if ((array[start_index] != target) and (array[end_index] != target) and ((end_index - start_index) < 2)):
        return -1
    elif (array[start_index] == target):
        return start_index
    elif (array[end_index] == target):
        return end_index
    if (len(array) == 1) and array[0] != target:
        return -1
    if (target > array[end_index]):
        return -1

    # if it is > target
    if (array[check_index] > target):
        # binary search that index to the bottom
        return binary_search(target, array, start_index=0, end_index=check_index)
    # if it is < target
    elif (array[check_index] < target):
        # binary search that index to the top
        return binary_search(target, array, start_index=check_index, end_index=end_index)
    elif array[check_index] == target:
        return check_index

    return -1

# values = [1,2,3,4,5]
# print("Index: ", binary_search(3, values))
