from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def binary_tree_path(root: Node) -> List[str]:
#     def dfs(node: Node, path: List[str]):
#         if node.left is None or node.right is Node:
#             res.append("->".join(path) + "->" + str(node.val))
#         for child in [node.left, node.right]:
#             if child is not None:
#                 dfs(child, path + [str(node.val)])

#     res = []
#     if root:
#         dfs(root, [])
#     return res


def binary_tree_path(root: Node) -> List[str]:
    def dfs(node: Node, path: List[str]):
        if node.left is None or node.right is Node:
            res.append("->".join(path) + "->" + str(node.val))
        for child in [node.left, node.right]:
            if child is not None:
                path.append(str(node.val))
                dfs(child, path)
                path.pop()

    res = []
    if root:
        dfs(root, [])
    return res


a = Node(1)
a.left = Node(2)
a.left.left = Node(3)
a.right = Node(4)

res = binary_tree_path(a)
print(res)
