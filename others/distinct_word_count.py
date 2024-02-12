import unittest


# Given a sentence, return distance word count in the sentence
def distinct_word_count(sentence: str) -> int:
    """
    Runtime: O(n)
    - O(n) to split the sentence into words
        where n is the length of the sentence
    - O(m) to split convert the list of sets into list
        where m is the number of word
    - O(1) to count the number of words in the list
    """
    if len(sentence) == 0:
        return 0
    return len(set(sentence.split(" ")))


# Given a sentence, return distance word count in the sentence.
# you are required to use a dictionary
def distinct_word_count_dict(sentence: str) -> int:
    """
    Runtime: O(n)
    - O(n) to split sentences into words
        where n is the length of the sentence
    - O(m) to iterate through each word
        where m is the number of words
    - O(1) to set and get element in the dictionary
    - O(1) to count the number of time in dictionary
    """
    if len(sentence) == 0:
        return 0
    words = sentence.split(" ")
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return len(word_dict)


class TestDistinctWordCount(unittest.TestCase):

    # Test Cases for test_all_distinct_words() function

    def test_all_distinct_words(self):
        self.assertEqual(distinct_word_count("Hello world"), 2)

    def test_some_repeated_words(self):
        self.assertEqual(distinct_word_count("Hello world world"), 2)

    def test_all_repeated_words(self):
        self.assertEqual(distinct_word_count("world world world world"), 1)

    def test_sentence_with_punctuation(self):
        # This test might fail depending on how you handle punctuation
        self.assertEqual(distinct_word_count("Hello, world! World is big."), 5)

    def test_empty_sentence(self):
        self.assertEqual(distinct_word_count(""), 0)

    # Test Case for distinct_word_count_dict() function
    def test2_all_distinct_words(self):
        self.assertEqual(distinct_word_count_dict("Hello world"), 2)

    def test2_some_repeated_words(self):
        self.assertEqual(distinct_word_count_dict("Hello world world"), 2)

    def test2_all_repeated_words(self):
        self.assertEqual(distinct_word_count_dict("world world world world"), 1)

    def test2_sentence_with_punctuation(self):
        # This test might fail depending on how you handle punctuation
        self.assertEqual(distinct_word_count_dict("Hello, world! World is big."), 5)

    def test2_empty_sentence(self):
        self.assertEqual(distinct_word_count_dict(""), 0)


if __name__ == "__main__":
    unittest.main()
