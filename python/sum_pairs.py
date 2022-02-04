def sum_pairs(arr, num):
    output = []
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if (i == j):
                continue
            if (arr[i] + arr[j] == num):
                output.append([arr[i], arr[j]])
    return output if len(output) > 0 else 'unable to find pairs'