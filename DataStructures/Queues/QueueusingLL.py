class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, data):
        newnode = Node(data)
        if self.head is None or self.tail is None:
            self.head = self.tail = newnode
            return f"{data} is enqueued"
        else:
            self.tail.next = newnode
            self.tail = newnode
            return f"{data} is enqueued"

    def dequeue(self):
        if self.head is None:
            return f"Queue is Empty"
        else:
            item = self.head.data
            self.head = self.head.next
            return f"{item} is dequeued"

    def peek(self):
        if self.head is None:
            return f"Queue is Empty"
        else:
            return self.head.data

    def isEmpty(self):
        return True if self.head else False

Q = Queue()
print(Q.enqueue(1))
print(Q.enqueue(2))
print(Q.enqueue(3))
print(Q.peek())    # Should return 1
print(Q.dequeue()) # Should return "1 is dequeued"
print(Q.isEmpty()) # Should return False
print(Q.dequeue()) # Should return "2 is dequeued"
print(Q.dequeue()) # Should return "3 is dequeued"
print(Q.isEmpty()) # Should return True
print(Q.peek())    # Should return "Queue is Empty"
print(Q.dequeue()) # Should return "Queue is Empty"