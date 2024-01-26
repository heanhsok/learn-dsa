import unittest
from typing import List
import sys

sys.path.append("../")
from utils.linked_list import Node, create_linked_list


def find_middle_of_linked_list(head: Node) -> int:
    """
    Input: 0 1 2 3 4
    Output: 2

    Input: 0 1 2 3 4 5
    Output: 3
    """
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.val


class Test(unittest.TestCase):
    def test_1(self):
        a = create_linked_list([0, 1, 2, 3, 4])
        return self.assertTrue(find_middle_of_linked_list(a), 2)

    def test_2(self):
        b = create_linked_list([0, 1, 2, 3, 4, 5])
        return self.assertTrue(find_middle_of_linked_list(b), 3)


if __name__ == "__main__":
    unittest.main()
