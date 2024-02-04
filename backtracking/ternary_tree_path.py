from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


# def ternary_tree_path(root: Node) -> List[str]:
#     def dfs(node, path):
#         if all(c is None for c in node.children):
#             res.append("->".join(path) + "->" + str(node.val))
#             return
#         for child in node.children:
#             if child is not None:
#                 dfs(child, path + [str(node.val)])

#     res = []
#     if root:
#         dfs(root, [])
#     return res


def ternary_tree_path(root: Node) -> List[str]:
    def dfs(node, path):
        if all(c is None for c in node.children):
            res.append("->".join(path) + "->" + str(node.val))
            return
        for child in node.children:
            if child is not None:
                path.append(str(node.val))
                dfs(child, path)
                path.pop()

    res = []
    if root:
        dfs(root, [])
    return res


a = Node(1)
b = Node(2)
d = Node(4)
a.children = [b, d, Node(6)]
b.children = [Node(3)]
d.children = [Node(5)]


a = ternary_tree_path(a)
print(a)
