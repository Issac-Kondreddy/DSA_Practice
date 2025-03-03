class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def insert_at_pos(self, data, pos):
        if pos<0:
            print("pos out of range")
            return
        if pos==0:
            self.insert_at_beginning(data)
            return
        current = self.head
        new_node = Node(data)
        while pos>1 and current is not None:
            pos -= 1
            current = current.next
        if current is None:
            print("pos out of range")
            self.insert_at_end(data)
            return
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end = " -->")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_end(50)
ll.insert_at_pos(40, 2)  # Insert 40 at position 2
ll.insert_at_pos(60, 10) # Position out of bounds, should insert at end
ll.print_list()
