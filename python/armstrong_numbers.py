# The first 24 exist in the first 20,000,000 integers
FIRST_24 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315]
def find_armstrong_numbers(numbers):
    return [n for n in numbers if is_armstrong_number(n)]

def is_armstrong_number(n):
    if n in FIRST_24:
        return True
    elif n < 20_000_000:
        return False
    else:
        exponent = len(str(n))
        n_as_list = list(str(n))
        sum = 0
        for num in n_as_list:
            sum += int(num) ** exponent
        return sum == n