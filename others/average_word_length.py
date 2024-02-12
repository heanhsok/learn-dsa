import unittest
from typing import Set


# given a sentence calculate average word length
# Example:
# input: 'Hello world programming'
# outptut: int((5 + 5 + 11) / 3) = 7
def avg_word_length(s: str) -> int:
    """
    Runtime: O(n)
    - O(n) to split the sentences into words
            where n is the length of the sentence
    - O(m) to iterate through and get length of each words
            where m is the number of words in the list
    """
    if len(s) <= 0:
        return 0
    words = s.split(" ")
    total_length_of_all_words = sum([len(word) for word in words])
    return int(total_length_of_all_words / len(words))


# Given a set of words, calculate the average word length
def avg_word_length_set(s: Set[str]) -> int:
    """
    Runtime: O(m)
        - O(m) to iterate through and get length of each words
            where m is the number of words in the list
    """
    if not s:
        return 0
    total_length = sum([len(word) for word in s])
    return int(total_length / len(s))


import unittest


class TestAverageWordLength(unittest.TestCase):

    def test_distinct_word_lengths(self):
        sentence = "Hello world programming"
        expected_average = int((5 + 5 + 11) / 3)
        self.assertEqual(avg_word_length(sentence), expected_average)

    def test_same_length_words(self):
        sentence = "cat bat hat"
        expected_average = int(3)  # All words are 3 letters long
        self.assertEqual(avg_word_length(sentence), expected_average)

    def test_mixed_length_words(self):
        sentence = "a bc def"
        expected_average = int((1 + 2 + 3) / 3)
        self.assertEqual(avg_word_length(sentence), expected_average)

    def test_empty_sentence(self):
        sentence = ""
        expected_average = 0  # No words in the sentence
        self.assertEqual(avg_word_length(sentence), expected_average)


class TestAverageLengthOfWords(unittest.TestCase):

    def test_different_length_words(self):
        word_set = {"Hello", "world", "programming", "Python"}
        expected_average = int((5 + 5 + 11 + 6) / 4)
        self.assertEqual(avg_word_length_set(word_set), expected_average)

    def test_same_length_words(self):
        word_set = {"cat", "bat", "hat", "mat"}
        expected_average = int(3)  # All words are 3 letters long
        self.assertEqual(avg_word_length_set(word_set), expected_average)

    def test_empty_set(self):
        word_set = set()
        expected_average = 0  # The set is empty
        self.assertEqual(avg_word_length_set(word_set), expected_average)

    def test_single_word(self):
        word_set = {"Python"}
        expected_average = int(6)  # Only one word in the set
        self.assertEqual(avg_word_length_set(word_set), expected_average)


if __name__ == "__main__":
    unittest.main()
