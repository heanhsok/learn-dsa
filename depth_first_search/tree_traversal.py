import io
import sys
import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: Node) -> Node:
    """
    LVR
    
    Input:
    #       2
    #      / \
    #     1   3
    Output: 123
    """
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.val, end=" ")
    in_order_traversal(root.right)


def pre_order_traversal(root: Node) -> None:
    """
    VLR
    
    Input:
    #       2
    #      / \
    #     1   3
    Output: 213
    """
    if root is None:
        return
    print(root.val, end=" ")
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def post_order_traversal(root: Node) -> None:
    """
    LRV
    
    Input:
    #       2
    #      / \
    #     1   3
    Output: 132
    """
    if root is None:
        return
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
    print(root.val, end=" ")


class Test(unittest.TestCase):
    def setUp(self):
        # Setup a test tree
        #       2
        #      / \
        #     1   3
        self.root = Node(2)
        self.root.left = Node(1)
        self.root.right = Node(3)

    def test_in_order_traversal(self):
        # Capture the output
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        in_order_traversal(self.root)

        # reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput.getvalue().strip(), "1 2 3")

    def test_pre_order_traversal(self):
        # Capture the output
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        pre_order_traversal(self.root)

        # reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput.getvalue().strip(), "2 1 3")

    def test_post_order_traversal(self):
        # Capture the output
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        post_order_traversal(self.root)

        # reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput.getvalue().strip(), "1 3 2")


if __name__ == "__main__":
    unittest.main()
