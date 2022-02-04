"""
Do the caesar shift!
"""
def caesar_cipher(string, shift_amount):
    """
    accepts the string to shift, the amount to shift it.
    qb's the shifting.
    """
    # split the string, iterate the list, convert as necessary
    shifted_string = shift(shift_amount)
    return ''.join(map(shifted_string, list(string)))

def shift(shift_amount):
    """
    function factory to create a function that called move letter with the
    correct amount of shift
    input: shift(5)
    output: function(x)
    """
    return lambda x: move_letter(x, shift_amount)

def move_letter(letter, shift_amount):
    """
    moves a letter the correct amount, looping around the end of the alphabet
    maintains the letter case
    """
    # //a = 97
    # //z = 122
    # //A = 65
    # //Z = 90
    code = ord(letter) # retrieve the code of the letter
    if (code >= 97 and code <= 122):
        # move the letter
        code += shift_amount
        if code > 122:
            code -= 26
        if code < 97:
            code += 26
    elif code >= 65 and code <= 90:
        code += shift_amount
        if code > 90:
            code -= 26
        if code < 65:
            code += 26
    else:
        return letter

    return chr(code)
