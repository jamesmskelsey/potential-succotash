def factorial(x):
    return 1 if x == 0 else x * factorial(x-1)

def palindrome(string, reversed=""):
    # we'll look at reversed, if it's not the same length as string
    #reversed += string[-(len(reversed))]
    if len(string) != len(reversed):
        # we haven't reversed it yet, we'll call palindrom again
        # we'll append the next letter of palindrome to reversed
        curr = len(reversed) + 1
        reversed += string[-(curr)]
        print(string[-(curr)])
        return palindrome(string, reversed)
 
    # we'll compare them and return our answer
    if len(string) == len(reversed) and string == reversed:
        print(string, reversed)
        return True
    elif len(string) == len(reversed) and string != reversed:
        print(string, reversed)
        return False
	
# I split this up some because to do it nicely recursively, I want to break it out in
# to some smaller functions
def bottles(num):
    sing_line(num)
    print(f"""No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, {num} bottles of beer on the wall.""")

def sing_line(num):
    if num > 0:
        print(f"""{plural_bottles(num)} of beer on the wall, {plural_bottles(num)} of beer.
Take one down and pass it around, {plural_bottles(num - 1).lower()} of beer on the wall.""")
        sing_line(num-1)

def plural_bottles(num):
    if num > 1:
        return f"{num} bottles"
    if num == 1:
        return "1 bottles"
    return "No more bottles"

ROMAN_TO_ARABIC_MAP = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

def roman_num(num, rta_map_item=0):
    (letter, value) = list(ROMAN_TO_ARABIC_MAP.items())[rta_map_item]
    #print(letter, value)
    if num - value > 0:
        return letter + roman_num(num - value, rta_map_item)
    if num - value < 0:
        return roman_num(num, rta_map_item + 1)
    else:
        return letter

# print(palindrome('racecar'))
# print(bottles(9))
# print(factorial(5))
# print(roman_num(2100))
