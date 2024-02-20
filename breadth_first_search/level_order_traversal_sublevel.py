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
	Input:
		1
	   / \
	  2   3
	 /\   |
	4  5  6
	|
	7
	ouptput: 
    [
        [1],
        [2,3],
        [4,5,6],
        [7]
    ]
	"""
    if root is None:
        return []
    res = []
    q = deque([root])
    while len(q) > 0:
        num_child = len(q)
        new_level = []
        for _ in range(num_child):
            node = q.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
        res.append(new_level)
    return res


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)

        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.left.left.left = Node(7)

        self.root.right.left = Node(6)

    def test_0(self):
        res = level_order_traverval(None)
        print(res)
        self.assertEqual(res, [])

    def test_1(self):
        expected_output = [[1], [2, 3], [4, 5, 6], [7]]
        res = level_order_traverval(self.root)
        print(res)
        self.assertEqual(res, expected_output)

    def test_2(self):
        res = level_order_traverval(Node(1))
        print(res)
        self.assertEqual(res, [[1]])


if __name__ == "__main__":
    unittest.main()
