from typing import List


class Node:
    val = None
    left_node = None
    right_node = None;

    def __init__(self, val):
        self.val = val


class DFS:
    result = []
    @staticmethod
    def traverse(root: Node):
        if root is None:
            return []
        left = DFS.traverse(root.left_node)
        right = DFS.traverse(root.right_node)
        print(root.val)
        res = []
        if left:
            res += left
        if right:
            res += right
        result = res.append(root.val)
        return res.append(root.val)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left_node = b
a.right_node = c
b.left_node = d
b.right_node = e

c.right_node = f
DFS.traverse(a)