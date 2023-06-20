class Node:
    """Representation of a node"""

    def __init__(self, node_value):
        self.node_value = node_value
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node
        self.start = node
        self.count = 1

    def add(self, value):
        new_node = Node(value)

        if self.count == 1:
            self.start.next = new_node
        self.head.next = new_node
        self.head = new_node
        self.count = self.count + 1

    def get(self, index):
        if self.count < index:
            raise IndexError('Index not found in Linked list')
        next_node = self.start
        node_count = 0
        while node_count < self.count:
            if node_count == index:
                return next_node.node_value
            next_node = next_node.next
            node_count = node_count + 1

    def print(self):
        if self.count == 1:
            print(str(self.start.node_value))
            return
        nodes = str(self.start.node_value)
        next_node = self.start.next
        while next_node:
            nodes += f" >> {str(next_node.node_value)}"
            next_node = next_node.next

        print(nodes)


linked_list = LinkedList(Node(1))
linked_list.add(2)
linked_list.add(3)
linked_list.add(50)
linked_list.add(3000)
linked_list.add(9)
linked_list.print()

print(linked_list.get(3))
