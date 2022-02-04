# Can you translate this driver code to unit tests?
from unittest import TestCase, main
from palindrome import palindrome
# This should return a bunch of trues
print(palindrome('racecar') == True)
print(palindrome('Noon') == True)
print(palindrome('ciVic') == True)
print(palindrome('nice') == False)
print(palindrome(434) == True)
print(palindrome(123) == False)
print(palindrome('bomb') == False)

print("The following should be True if you're trying to do the extra portion of this challenge")
print(palindrome('Sore was I ere I saw Eros.') == True)
print(palindrome('A man, a plan, a canal -- Panama') == True)

class PalindromeTestCase(TestCase):
    def test_returns_a_bool(self):
        self.assertEqual(type(palindrome("dd")), bool)

    def test_returns_true_if_given_palindrom(self):
        self.assertEqual(palindrome("racecar"), True)    
        self.assertEqual(palindrome('Sore was I ere I saw Eros.'), True)

if __name__ == '__main__':
    main()

