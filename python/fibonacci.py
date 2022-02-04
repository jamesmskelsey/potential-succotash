
import math

# Using Binet's formula to achieve O(1) time complexity for finding the nth fibonacci number
# https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula


def fibonacci(n):
    onePlus = pow((1 + math.sqrt(5)) / 2, n)
    oneMinus = pow((1 - math.sqrt(5)) / 2, n)
    return math.trunc((onePlus - oneMinus) / math.sqrt(5))


print(fibonacci(100))
