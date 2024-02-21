from collections import deque
import unittest
import sys
import io


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Node) -> int:
    """
	# Given a binary tree, find the depth of the shallowest leaf node.
	Input:
		1
	   / \
	  2   3
	 /\   |
	4  5  6
	|  
	7  
	ouptput: 
	2
	"""
    if root is None:
        return 0
    depth = 0
    q = deque([root])
    while len(q) > 0:
        num = len(q)
        for _ in range(num):
            node = q.popleft()
            if node.left is None and node.right is None:
                return depth
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
        depth += 1
    return depth


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
        res = min_depth(None)
        print(res)
        self.assertEqual(res, 0)

    def test_1(self):
        expected_output = 2
        res = min_depth(self.root)
        print(res)
        self.assertEqual(res, expected_output)

    def test_2(self):
        res = min_depth(Node(1))
        print(res)
        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()
