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
    ouptput: 1 2 3 4 5 6 7
    """

    q = deque([root])
    while len(q) > 0:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


class Test(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)

        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.left.left.left = Node(7)

        self.root.right.left = Node(6)

    def test_1(self):
        # Capture the output
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        level_order_traverval(self.root)

        # reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput.getvalue().strip(), "1 2 3 4 5 6 7")


if __name__ == "__main__":
    unittest.main()
