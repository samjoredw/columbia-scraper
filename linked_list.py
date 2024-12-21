class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.header = Node(None, None)
        self.header.next = self.header

    def add(self, element):
        new_node = Node(element, None)
        new_node.next = self.header.next
        self.header.next = new_node