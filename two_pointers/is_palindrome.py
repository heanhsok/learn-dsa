import unittest


# def is_palindrome(s: str) -> bool:
#     return s.replace(" ", "").lower()[::] == s.replace(" ", "").lower()[::-1]


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while not s[l].isalnum():
            l += 1
        while not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_simple_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("a man a plan a canal panama"))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))

    def test_non_palindrome_with_punctuation(self):
        self.assertFalse(is_palindrome("This is, obviously, not a palindrome!"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("No lemon, no melon"))


if __name__ == "__main__":
    unittest.main()
