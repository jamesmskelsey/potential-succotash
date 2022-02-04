from functools import reduce

def credit_check(str):
    # Break the string in to a list of digits, double every other digit, send each digit to sum_digits to add the digits
    # together if needed
    digit_break_down = [sum_digits(x) for x in [(int(n) * 2) if idx % 2 == 0 or idx == 0 else int(n) for (idx,n) in enumerate(list(str))]]
    
    # Reduce the list by adding together all the values, check to see if the number is valid by checking it can be evenly divided by 10
    # And return the valid/invalid string
    return "The number is valid!" if (sum(digit_break_down) % 10) == 0 else "The number is invalid!"

def sum_digits(element):
    # adding the digits is the same as subtracting 9
    # Thanks, Kana Pankey!
    return element - 9 if element > 9 else element
    

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

# print(credit_check("5541808923795240"))
