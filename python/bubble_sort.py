"""
Basic implementation of bubble sort
"""

def bubble_sort(arr):
    """
    uses bubble sort to sort an array of integers
    """
    prev = 0
    curr = 1
    swap_made = False
    # iterate across the array

    # check if the array is sorted
    while not swap_made:
        swap_made = False if swap_made else True
        ## if the prev > curr
        if arr[prev] > arr[curr]:
            ### swap them
            arr[prev], arr[curr] = arr[curr], arr[prev]
            ### increment swaps
            swap_made = True
        else:
            prev += 1
            curr += 1

        if curr > len(arr):
            prev = 0
            curr = 1

    return arr

print(bubble_sort([1, 0, 2, 5, 9]))
