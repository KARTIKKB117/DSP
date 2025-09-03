class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        