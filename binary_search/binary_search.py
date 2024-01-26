from typing import List
import unittest


def binary_search(arr: List[int], target: int) -> int:
    """
    Perform search using binary search algorithm
    to find index of a specific element (target)
    in a sorted list (arr)

    Parameters:
    arr (List[int]): the sorted list of integer to search
    target (int): the integer to search for in the list

    Returns:
    int: return index of the integer if found, else return -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([1], 2), -1)

    def test_even_number_of_elements_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)

    def test_even_number_of_elements_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 5), -1)

    def test_odd_number_of_elements_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_odd_number_of_elements_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_negative_numbers_and_zero(self):
        self.assertEqual(binary_search([-3, -2, -1, 0, 1, 2, 3], -2), 1)

    def test_needle_at_boundaries_first(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_needle_at_boundaries_last(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_with_duplicate_elements(self):
        self.assertIn(binary_search([1, 1, 2, 2, 3, 3], 2), [2, 3])

    def test_non_sorted_list(self):
        self.assertEqual(binary_search([0, 1, 4, 2, 5], 3), -1)


if __name__ == "__main__":
    unittest.main()
