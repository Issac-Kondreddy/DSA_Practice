class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyCLL:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
        else:
            newnode.next = self.head
            newnode.prev = self.head.prev
            self.head.prev.next = newnode
            self.head.prev = newnode
            self.head = newnode
    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
        else:
            current = self.head
            while True:
                current = current.next
                if current.next == self.head:
                    break
            newnode.next = self.head
            newnode.prev = current
            current.next = newnode
            self.head.prev = newnode
    def insert_at_pos(self, data, pos):
        if pos < 0:
            print("pos cannot be negative")
            return
        if pos>=self.length():
            print("pos cannot be greater than the length of the list")
            return
        if pos==0:
            self.insert_at_beginning(data)
        newnode = Node(data)
        k = 0
        current = self.head
        while k < pos:
            current = current.next
            k += 1
        if current.next == self.head:
            self.insert_at_end(data)
        newnode.next = current.next
        newnode.prev = current
        current.next.prev = newnode
        current.next = newnode
    def display(self):
        current = self.head
        print("Head", end=" <-> ")
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("Tail")
    def length(self):
        if self.head is None:
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count
    def delete_at_beginning(self):
        if self.head is None:
            print("list is empty")
            return
        elif self.head.next == self.head:
            print(f"Head Node Deleted {self.head.data} and list is empty")
            self.head = None
            return
        else:
            current = self.head
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
            print(f"Node Deleted {current.data}")
    def delete_at_end(self):
        if self.head is None:
            print("list is empty")
            return
        elif self.head.next == self.head:
            print(f"Head Node Deleted {self.head.data} and list is empty")
            self.head = None
            return
        else:
            current = self.head
            while True:
                current = current.next
                if current.next == self.head:
                    break
            self.head.prev = current.prev
            current.prev.next = self.head
            print(f"Node Deleted {current.data}")
    def delete_at_pos(self, pos):
        if pos < 0:
            print("pos cannot be negative")
            return
        if pos==0:
            self.delete_at_beginning()
        if pos==self.length():
            self.delete_at_end()
        k = 0
        current = self.head
        while k < pos:
            k = k + 1
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        print(f"Node Deleted {current.data}")
    def search(self, data):
        if self.head is None:
            print("list is empty")
            return
        else:
            current = self.head
            while True:
                current = current.next
                if current.data == data:
                    print(f"Node Found {data}")
                    return True
                if current.next == self.head:
                    print(f"Node not Found {data}")
                    return False


DCLL = DoublyCLL()
DCLL.insert_at_beginning(1)
DCLL.display()
DCLL.insert_at_end(2)
DCLL.insert_at_end(3)
DCLL.display()
DCLL.insert_at_beginning(4)
DCLL.display()
DCLL.insert_at_end(5)
DCLL.display()
DCLL.insert_at_pos(6,2)
DCLL.display()
print(DCLL.length())
DCLL.delete_at_beginning()
DCLL.display()
DCLL.delete_at_end()
DCLL.display()
DCLL.delete_at_pos(2)
DCLL.display()
DCLL.search(3)
DCLL.search(4)
