class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        newnode = Node(data)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        newnode = Node(data)
        while current.next is not None:
            current = current.next
        newnode.prev = current
        current.next = newnode
    def insert_at_pos(self, data, pos):
        current = self.head
        index = 0
        while current is not None and index <  pos-1:
            current = current.next
            index += 1
        if current is None:
            print("Index out of range")
            return
        newnode = Node(data)
        newnode.next = current.next
        newnode.prev = current
        if current.next is not None:
            current.next.prev = newnode
        current.next = newnode

    def length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def search(self, data):
        current = self.head
        pos = 0
        while current is not None:
            if current.data == data:
                return f"Element {data} was found at position {pos}"
            current = current.next
            pos += 1
        return "Element not found"

    def print_list(self):
        current = self.head
        print("Head", end = " <-> ")
        while current is not None:
            print(current.data, end = " <-> ")
            current = current.next
        print("Null")
    def print_reverse(self):
        current = self.head
        while current.next is not None:
            current = current.next
        print("Tail", end = " <-> ")
        while current is not None:
            print(current.data, end = " <-> ")
            current = current.prev
        print("Head")

    def delete_at_beginning(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None
            return
        self.head =  self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None

    def delete_at_pos(self, pos):
        current = self.head
        index = 0
        if pos==0:
            self.delete_at_beginning()
            return
        while current is not None and index < pos:
            current = current.next
            index += 1
        if current is None:
            print("Index out of range")
            return
        if current.next is not None:
            current.next.prev = current.prev
        if current.prev is not None:
            current.prev.next = current.next



dll = DoubleLinkedList()
dll.insert_at_beginning(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.insert_at_beginning(6)
dll.insert_at_beginning(7)
dll.insert_at_beginning(8)
print(f"The Length of linked list is : {dll.length()}")
dll.print_list()
dll.print_reverse()
print(dll.search(2))
dll.delete_at_beginning()
dll.delete_at_end()
dll.print_list()
dll.delete_at_pos(2)
dll.print_list()
dll.print_reverse()
