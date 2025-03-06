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
    def delete_at_beginning(self):
        if self.head is None:
            return "List is empty"
        self.head = self.head.next
    def delete_at_end(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
    def delete_at_pos(self, pos):
        if self.head is None:
            return "List is empty"
        current = self.head
        if pos==0:
            self.delete_at_beginning()
            return
        k = 0
        while k < pos-1 and current.next is not None:
            current = current.next
            k += 1
        if current.next is None:
            print("Pos out of range")
            return
        current.next = current.next.next

    def reverselist(self):
        if self.head is None:
            return "List is empty"
        current = self.head
        prev = None
        next_node = None
        while current is not None:
            next_node= current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def length(self):
        if self.head is None:
            return "List is empty"
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, data):
        if self.head is None:
            return "List is empty"
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
        print("Head", end = " -> ")
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
        print("NULL")

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_end(50)
ll.insert_at_pos(40, 2)  # Insert 40 at position 2
ll.insert_at_pos(60, 10) # Position out of bounds, should insert at end

ll.print_list()  # Expected: 30 --> 20 --> 40 --> 10 --> 50 --> 60 --> None

ll.delete_at_beginning()
ll.print_list()  # Expected: 20 --> 40 --> 10 --> 50 --> 60 --> None

ll.delete_at_end()
ll.print_list()  # Expected: 20 --> 40 --> 10 --> 50 --> None
print(ll.search(50))
print(ll.length())
ll.delete_at_pos(2)
ll.print_list()  # Expected: 20 --> 40 --> 50 --> None

ll.reverselist()
ll.print_list()


