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


def to_roman(num):
    output = ""
    # iterate our list of possible subs
    for letter, arabic in ROMAN_TO_ARABIC_MAP.items():
      for _ in range(num // arabic):
        # sub, and decrement the input number
        output += letter
        num -= arabic
    return output
