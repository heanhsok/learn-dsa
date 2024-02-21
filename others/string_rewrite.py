import unittest


def string_rewrite(s: str) -> str:
    """
    count the number of times each character appears in a string
    and rewrite the string in that format.
    Eg. "I am back." should become "i1 2a2m1b1c1k1.1"

    Runtime: O(n)
    - O(n) to convert the sentence to lower case
    - O(n) to iterate through each character
    - O(1) to set and get element in the dictionary
    - O(m) to iterate through each k,v pair in the dictionary
    """
    word_count_dict = {}
    s_lower = s.lower()
    for c in s_lower:
        word_count_dict[c] = word_count_dict.get(c, 0) + 1
    new_s = ""
    for k, v in word_count_dict.items():
        new_s += f"{k}{v}"
    return new_s


class Test(unittest.TestCase):
    def test_0(self):
        input = "I am back."
        expected_output = "i1 2a2m1b1c1k1.1"
        output = string_rewrite(input)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
