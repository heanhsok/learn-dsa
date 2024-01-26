import unittest
from typing import List


def find_first_true(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    first_true = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            first_true = mid
            right = mid - 1
        else:
            left = mid + 1
    return first_true


class Test(unittest.TestCase):
    def test_single_element_found(self):
        return self.assertTrue(find_first_true([False, False, True, True, True]), 2)

    def test_element_not_found(self):
        return self.assertTrue(find_first_true([False, False]), -1)


if __name__ == "__main__":
    unittest.main()
