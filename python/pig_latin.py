"""
translate a phrase to pig-latin.
1. Translate
2. Keep punctuation
3. Keep capitalization
"""
import re

def translate(phrase):
    """
    splits phrase into a list, sends each word to translate word
    """
    return " ".join([translate_word(word) for word in phrase.split()])

def is_vowel_word(word):
    """
    Returns the match object from looking for a vowel at the beginning of the word
    """
    re_vowel_words = re.compile(r"^[aeiou]")
    return re_vowel_words.search(word)

def is_qu_word(word):
    """
    returns the match object from finding a 'qu' at the beginning of a word
    """
    re_translate_qu_words = re.compile(r"^.*qu")
    return re_translate_qu_words.search(word)

def is_constonant_word(word):
    """
    returns the match object from finding constonants at the beginning of a word
    """
    re_consonant_words = re.compile(r"^[^aeiou]*")
    return re_consonant_words.search(word)

def translate_word(word):
    """
    split a phrase in to multiple words
    submit that to a word translator
    """
    # set up output
    output = ""
    # remember punctuation
    punctuation = ""
    re_punctuation = re.compile(r"[^\w]*$")
    # remember if upper
    was_upper = is_upper(word)
    # move to lowercase
    word = word.lower()
    # set aside punc, remove it from the string
    punctuation = re_punctuation.search(word).group(0)
    word = re_punctuation.sub("", word)
    # translate the words with regexes
    if is_vowel_word(word):
        output = f"{word}ay"
    elif is_qu_word(word):
        match = is_qu_word(word).group(0)
        output = word[len(match):] + match + "ay"
    elif is_constonant_word(word):
        match = is_constonant_word(word).group(0)
        output = word[len(match):] + match + "ay"
    # put the word/puncuation back together
    output += punctuation
    # return the capitalized if necessary word
    return capitalize(output) if was_upper else output

def is_upper(word):
    """
    checks if the only the first character of a word is uppercase
    """
    return word[0].isupper()

def capitalize(word):
    """
    returns the word with the first letter capitalized
    """
    return word[0].upper() + word[1:]
