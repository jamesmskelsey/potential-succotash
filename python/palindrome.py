import re
def palindrome(word):
    # Write code here
    not_letters = re.compile(r"[^A-Za-z0-9]")
    if (type(word) == str):
        word = word.lower()
    word = re.sub(not_letters, "", str(word))
    return ''.join(list(word)[::-1]) == word

print(palindrome("Sore was I ere I saw Eros."))
