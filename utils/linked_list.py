from typing import List


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr: List[int]) -> Node:
    a = Node(arr[0])
    c = a
    for i in range(1, len(arr)):
        c.next = Node(arr[i])
        c = c.next
    return a


def traverse_linked_list(node: Node) -> None:
    c = node
    while c:
        print(c.val)
        c = c.next
