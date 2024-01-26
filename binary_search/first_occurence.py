from typing import List
import unittest


def find_first_occurence(arr: List[int], target: int) -> int:
    """
    Input:
    arr = [1, 3, 3, 3, 3, 5, 6, 10, 10, 10, 100]
    target = 3

    Output: 1
    """
    left, right = 0, len(arr) - 1
    first_occurence = -1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            first_occurence = mid
            right = mid - 1
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurence


class Test(unittest.TestCase):
    def test_1(self):
        return self.assertTrue(
            find_first_occurence([1, 3, 3, 3, 3, 5, 6, 10, 10, 10, 100], 3), 1
        )

    def test_2(self):
        return self.assertTrue(
            find_first_occurence([2, 3, 5, 7, 11, 13, 17, 19], 6), -1
        )


if __name__ == "__main__":
    unittest.main()
