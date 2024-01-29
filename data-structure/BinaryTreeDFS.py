class Node:
    val = None
    left_node = None
    right_node = None;

    def __init__(self, val):
        self.val = val


class DFC:
    root = None
    stack = []

    def __init__(self, root):
        self.root = root
        self.stack = [root]

    def traverse(self):
        if self.root is None:
            return []
        while len(self.stack) > 0:
            current = self.stack.pop()
            print(current.val)
            if current.right_node:
                self.stack.append(current.right_node)
            if current.left_node:
                self.stack.append(current.left_node)


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

dfc = DFC(a)
dfc.traverse()
