"""
Tests for the pig latin translator
"""
from unittest import TestCase, main

from pig_latin import translate

class TranslateTestCases(TestCase):
    """
    Tests the translate function for pig latin
    """
    def test_translates_word_beginning_with_a_vowel(self):
        """
        adds ay
        """
        res = translate('apple')
        expected = "appleay"
        self.assertEqual(res, expected)

    def test_retains_punctuation(self):
        """
        does not remove punctuation marks
        """
        res = translate('apples!')
        expected = "applesay!"
        self.assertEqual(res, expected)

    def test_retains_capitalization(self):
        """
        if given a capital lettered word, it returns it the same
        """
        res = translate('Apples')
        expected = "Applesay"
        self.assertEqual(res, expected)

    def test_translates_consonant_words(self):
        """
        can check for single consnants
        """
        res = translate('banana')
        expected = "ananabay"
        self.assertEqual(res, expected)

    def test_translates_words_with_multiple_consonants(self):
        """
        like school, cherry
        """
        res = translate('school')
        expected = 'oolschay'
        self.assertEqual(res, expected)

    def test_translates_qu_words(self):
        """
        qu should get treated as a single phoneme
        """
        res = translate('quick')
        expected = 'ickquay'
        self.assertEqual(res, expected)

    def test_translates_sentences(self):
        """
        translates all the words in a sentence
        """
        res = translate('the quick brown fox')
        expected = 'ethay ickquay ownbray oxfay'
        self.assertEqual(res, expected)

if __name__ == "__main__":
    main()
