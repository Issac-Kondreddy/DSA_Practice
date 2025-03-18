class Queue:
    def __init__(self):
        self.elements = []
        self.max_size = 100
    def enqueue(self, data):
        self.elements.append(data)
        return f"Item Added {data}"
    def dequeue(self):
        if len(self.elements)==0:
            return "Queue is Empty"
        element = self.elements.pop(0)
        return f"{element} removed"
    def front(self):
        return self.elements[0]
    def isEmpty(self):
        return len(self.elements)==0
    def isFull(self):
        return len(self.elements)==self.max_size
    def Display(self):
        print("Head", end = " <- ")
        for i in range(0, len(self.elements)):
            print(self.elements[i], end = " <- ")
        print("Tail")

Q = Queue()
print(Q.enqueue(1))
print(Q.enqueue(2))
print(Q.dequeue())
print(Q.front())
print(Q.enqueue(3))
print(Q.enqueue(4))
print(Q.enqueue(5))
Q.Display()