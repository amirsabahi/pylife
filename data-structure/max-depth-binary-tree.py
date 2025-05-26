class Node:
    value:None
    left_node:None
    right_node:None

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

class MaxDepth:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left_node)
        right_depth = self.maxDepth(root.right_node)

        return max(left_depth, right_depth) + 1
    

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(6)

root.left_node = node2
root.right_node = node3
node2.left_node = node4
node2.right_node = node5
node5.left_node = node7
node4.right_node = node6


md = MaxDepth()
print(md.maxDepth(root))