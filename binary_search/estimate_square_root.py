from typing import List
import unittest


def estimate_square_root(n: int) -> int:
    """
    Input: 16
    Output: 4

    Input: 8
    Output: 2
    """
    if n == 0:
        return 0

    left, right = 1, n
    sqrt = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        if mid * mid <= n:
            sqrt = mid
            left = mid + 1
        else:
            right = mid - 1
    return sqrt


class Test(unittest.TestCase):
    def test_1(self):
        return self.assertTrue(estimate_square_root(16), 1)

    def test_2(self):
        return self.assertTrue(estimate_square_root(8), 2)


if __name__ == "__main__":
    unittest.main()
