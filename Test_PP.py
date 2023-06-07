import unittest
from Python_Programming import is_palindrome

class Test(unittest.TestCase):

    def test_Func(self):
        word = 'reconocer'
        result = is_palindrome(word)
        self.assertEqual(result, f"Es un palindromo=>, {word}")

if __name__ == "__main__":
    unittest.main()