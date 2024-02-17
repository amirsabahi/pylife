class Node:
    val = None
    left_node = None
    right_node = None

    def __init__(self, val):
        self.val = val


class BFS:
    @staticmethod
    def search(root, search_key):
        if root is None:
            return []
        queue = [root]

        while len(queue) > 0:
            current = queue.pop(0)
            if current.val == search_key:
                return True

            if current.left_node:
                queue.append(current.left_node)

            if current.right_node:
                queue.append(current.right_node)
        return False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

a.left_node = b
a.right_node = c
b.left_node = d
b.right_node = e
c.right_node = f
f.left_node = g

if BFS.search(a, "g"):
    print("Key found!")
else:
    print("Key not found!")
