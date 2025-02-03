class Node:
    value = None
    next = None
    def __init__(self, value):
        self.value = value


class LinkedList:
    start=None
    head=None
    count= 0

    def add(self, node:Node):
        if self.count == 0:
            self.start=node
            self.head=self.start
            self.count = 1
            return True
        if self.count == 1:
            self.start.next = node
        self.head.next = node
        self.head = node
        self.count = self.count + 1
        return True



class Merge:
    def mergeToLinkedList(self, linkedList1:LinkedList, linkedList2:LinkedList):
        point1 = None
        point2 = None


        new_linkedList = LinkedList()
        next1 = linkedList1.start
        next2 = linkedList2.start
        while next1 and next2:
            if next1.value<= next2.value:
                new_linkedList.add(Node(next1.value))
                next1 = next1.next
            else:
                new_linkedList.add(Node(next2.value))
                next2 = next2.next

        while next1:
                  new_linkedList.add(Node(next1.value)) 
                  next1 = next1.next

        while next2:
                  new_linkedList.add(Node(next2.value)) 
                  next2 = next2.next
        nodes =''
        next_node =new_linkedList.start
        while next_node:
            nodes += f" >> {str(next_node.value)}"
            next_node = next_node.next

        print(nodes)  

linkedList1 = LinkedList()
linkedList1.add(Node(1))
linkedList1.add(Node(3))
linkedList1.add(Node(5))
linkedList1.add(Node(7))

linkedList2 = LinkedList()
linkedList2.add(Node(2))
linkedList2.add(Node(4))
linkedList2.add(Node(5))

merge = Merge() 

merge.mergeToLinkedList(linkedList1, linkedList2)