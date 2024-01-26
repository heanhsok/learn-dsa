import unittest


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Node) -> int:
    def dfs(node: Node) -> int:
        if node is None:
            return 0
        return max(dfs(node.left), dfs(node.right)) + 1

    if root:
        return dfs(root) - 1
    else:
        return 0


class Test(unittest.TestCase):
    def test_1(self):
        a = Node(1)
        a.right = Node(2)
        a.right.right = Node(3)
        a.right.right.left = Node(4)
        self.assertEqual(max_depth(a), 3)

    def test_2(self):
        a = None
        self.assertEqual(max_depth(a), 0)


if __name__ == "__main__":
    unittest.main()
