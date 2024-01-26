import unittest
from typing import List


def find_first_not_smaller(arr: List[int], target: int) -> int:
    """
    Input
    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2

    Output:
    1
    """
    left, right = 0, len(arr) - 1
    first_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            first_index = -1
            right = mid - 1
        else:
            left = mid + 1
    return first_index


class Test(unittest.TestCase):
    def test_1(self):
        return self.assertTrue(find_first_not_smaller([1, 3, 3, 5, 8, 8, 10], 2), 1)

    def test_2(self):
        return self.assertTrue(
            find_first_not_smaller([2, 3, 5, 7, 11, 13, 17, 19], 6), 3
        )


if __name__ == "__main__":
    unittest.main()
