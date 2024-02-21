from collections import deque
import unittest
import sys
import io


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Node) -> None:
    """
	# Given a binary tree, return the rightmost node of each level.
	# It should be noted that at each level there can only be at most one rightmost node.
	Input:
		1
	   / \
	  2   3
	 /\   |
	4  5  6
	|  
	7  
	ouptput: 
	[1, 3, 6, 7]
	"""
    if root is None:
        return []
    res = []
    q = deque([root])
    while len(q) > 0:
        num = len(q)
        # add the first element in the queue
        # which is the right most element
        res.append(q[0].val)
        for _ in range(num):
            node = q.popleft()
            # go from right to left
            for child in [node.right, node.left]:
                if child:
                    q.append(child)
    return res


# solution: 1
# def right_side_view(root: Node) -> None:
#     if root is None:
#         return []

#     res = []
#     q = deque([root])
#     while len(q) > 0:
#         num = len(q)
#         new_level = deque()
#         for _ in range(num):
#             node = q.popleft()
#             new_level.append(node.val)
#             for child in [node.left, node.right]:
#                 if child:
#                     q.append(child)
#         rightmost = new_level.pop()
#         res.append(rightmost)
#     return res


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)

        self.root.left.left = Node(4)
        self.root.left.left.left = Node(7)

        self.root.left.right = Node(5)

        self.root.right.left = Node(6)

    def test_0(self):
        res = right_side_view(None)
        print(res)
        self.assertEqual(res, [])

    def test_1(self):
        expected_output = [1, 3, 6, 7]
        res = right_side_view(self.root)
        print(res)
        self.assertEqual(res, expected_output)

    def test_2(self):
        res = right_side_view(Node(1))
        print(res)
        self.assertEqual(res, [1])


if __name__ == "__main__":
    unittest.main()
