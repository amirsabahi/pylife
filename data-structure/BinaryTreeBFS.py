class Node:
    val = None
    left_node = None
    right_node = None

    def __init__(self, val):
        self.val = val

class BFS:
    def traverse(self, root):
        if root is None:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.val)
            result.append(current.val)
            if current.left_node:
                queue.append(current.left_node)
            if current.right_node:
                queue.append(current.right_node)
        return result
    

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.left_node = b
a.right_node= c
b.left_node = d
b.right_node = e
c.right_node = f

bfs = BFS()
bfs.traverse(a)