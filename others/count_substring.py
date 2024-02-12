import unittest


# count the number of time a substring appear in a string
def count_substring_occurrences(s: str, sub_s: str) -> int:
    """
    Runtime: O(m*n) where
        - m is the length of the string
        - n is the length of the substring

    """
    return s.count(sub_s)


class TestCountSubstringOccurrences(unittest.TestCase):

    def test_no_occurrences(self):
        self.assertEqual(count_substring_occurrences("hello world", "abc"), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(count_substring_occurrences("hello hello world", "hello"), 2)

    def test_overlapping_occurrences(self):
        # Note: Python's count does not consider overlapping occurrences
        self.assertEqual(count_substring_occurrences("abababa", "aba"), 2)

    def test_empty_main_string(self):
        self.assertEqual(count_substring_occurrences("", "test"), 0)

    def test_empty_substring(self):
        # Counting an empty substring returns the length of the string plus one in Python
        self.assertEqual(count_substring_occurrences("hello", ""), 6)


if __name__ == "__main__":
    unittest.main()
