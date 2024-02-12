import unittest
from typing import List, Dict
from collections import Counter

# Given a list of ints, balance the list so that each int appears equally in the list. Return a dictionary where the key is the int and the value is the count needed to balance the list.
# Example
# input => output
# [1, 1, 2] => {2: 1}
# [1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}


def balance_list(arr: List[int]) -> Dict[int, int]:
    """
    Runtime:
    - O(n) for Counter() function which counts the freq of each item
    - O(klogk) for .most_common() function which sorts the the counts
    - O(n) iterate through the sorted counts
    """

    counters = Counter(arr).most_common()
    balancer = {}
    for i, (ele, count) in enumerate(counters):
        if i == 0:
            max_count = count
        else:
            balancer[ele] = max_count - count
    return balancer


# improvment of the above by removing the sorting part
def balance_list2(arr: List[int]) -> Dict[int, int]:
    """
    Runtime:
    - O(n) for Counter() function which counts the freq of each item
    - O(n) for max() function which finds the max value
    - O(n) to iterate through counter objects
    """
    counters = Counter(arr)
    max_num = max(counters.values())
    return {key: max_num - val for key, val in counters.items() if max_num - val > 0}


class TestBalanceList(unittest.TestCase):

    def test_balance_list_simple(self):
        input_list = [1, 1, 2]
        expected_output = {2: 1}
        result = balance_list(input_list)
        self.assertEqual(result, expected_output)

    def test_balance_list_complex(self):
        input_list = [1, 1, 1, 5, 3, 2, 2]
        expected_output = {5: 2, 3: 2, 2: 1}
        result = balance_list(input_list)
        self.assertEqual(result, expected_output)


class TestBalanceList2(unittest.TestCase):

    def test_balance_list2_simple(self):
        input_list = [1, 1, 2, 3]
        expected_output = {2: 1, 3: 1}
        result = balance_list2(input_list)
        self.assertEqual(result, expected_output)

    def test_balance_list2_complex(self):
        input_list = [1, 1, 1, 5, 3, 2, 2]
        expected_output = {5: 2, 3: 2, 2: 1}
        result = balance_list2(input_list)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
