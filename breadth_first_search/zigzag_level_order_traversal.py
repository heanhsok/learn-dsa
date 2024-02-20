from collections import deque
import unittest
import sys
import io


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traverval(root: Node) -> None:
    """
    # Given a binary tree, return its level order traversal but in alternate left to right order.
	Input:
		1
	   / \
	  2   3
	 /\   |
	4  5  6
	|  |
	7  8
	ouptput: 
	[
		[1],
		[3,2],
		[4,5,6],
		[8,7]
	]
	"""
    if root is None:
        return []
    res = []
    q = deque([root])
    left_to_right = True
    while len(q) > 0:
        new_level = deque()
        num = len(q)
        for _ in range(num):
            node = q.popleft()
            if left_to_right:
                new_level.append(node.val)
            else:
                new_level.appendleft(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
        res.append(list(new_level))
        left_to_right = not left_to_right
    return res


# def level_order_traverval(root: Node) -> None:
#     if root is None:
#         return []
#     res = []
#     q = deque([root])
#     flip = False
#     while len(q) > 0:
#         new_level = []
#         num = len(q)
#         for _ in range(num):
#             node = q.popleft()
#             new_level.append(node.val)
#             for child in [node.left, node.right]:
#                 if child:
#                     q.append(child)
#         if flip:
#             new_level.reverse()
#         res.append(new_level)
#         flip = ~flip
#     return res


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)

        self.root.left.left = Node(4)
        self.root.left.left.left = Node(7)

        self.root.left.right = Node(5)
        self.root.left.right.left = Node(8)

        self.root.right.left = Node(6)

    def test_0(self):
        res = level_order_traverval(None)
        print(res)
        self.assertEqual(res, [])

    def test_1(self):
        expected_output = [[1], [3, 2], [4, 5, 6], [8, 7]]
        res = level_order_traverval(self.root)
        print(res)
        self.assertEqual(res, expected_output)

    def test_2(self):
        res = level_order_traverval(Node(1))
        print(res)
        self.assertEqual(res, [[1]])


if __name__ == "__main__":
    unittest.main()
