class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
            newnode.next = self.head
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            newnode = Node(data)
            newnode.next = self.head
            current.next = newnode
            self.head = newnode
    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head  = newnode
            newnode.next = self.head
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            newnode.next = self.head
            current.next = newnode
    def insert_at_pos(self, data, pos):
        if pos==0 or self.head is None:
            return self.insert_at_beginning(data)
        else:
            current = self.head
            i = 1
            while current.next is not self.head and i < pos:
                current = current.next
                i += 1
            newnode = Node(data)
            newnode.next = current.next
            current.next = newnode
    def display(self):
        if self.head is None:
            return "List is empty"
        current = self.head
        print("Head", end="->")
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print("Head")
    def delete_at_beginning(self):
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next is not self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next
        return
    def delete_at_end(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is self.head:
            self.head = None
            return "List is empty after deleting last node"
        current = self.head
        while current.next.next is not self.head:
            current = current.next
        current.next = self.head
        return "Last Node deleted"
    def delete_node(self, data):
        if self.head is None:
            return "List is empty"
        if self.head.data == data:
            self.delete_at_beginning()
        current = self.head
        while True:
            if current.next == self.head:
                return "Node not found"
            if current.next.data == data:
                if current.next.next is self.head:
                    return self.delete_at_end()
                current.next = current.next.next
                return
            current = current.next


SCLL = SinglyCircularLinkedList()
SCLL.insert_at_beginning(1)
SCLL.insert_at_beginning(2)
SCLL.insert_at_beginning(3)
SCLL.display()
SCLL.insert_at_end(4)
SCLL.insert_at_end(5)
SCLL.insert_at_end(6)
SCLL.display()
SCLL.insert_at_pos(7, 3)
SCLL.display()
SCLL.delete_at_beginning()
SCLL.display()
SCLL.delete_at_end()
SCLL.display()
SCLL.delete_node(7)
SCLL.display()

