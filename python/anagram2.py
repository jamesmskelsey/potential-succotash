# Don't forget to run the tests (and create some of your own)
from character_match import is_character_match

def anagrams_for(word, list_of_words):
		return list(filter(lambda el : is_character_match(el, word), list_of_words))
