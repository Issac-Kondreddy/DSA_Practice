class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self, item):
        newnode = Node(item)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def peek(self):
        if self.head is None:
            return "Stack is Empty"
        return self.head.data
    def pop(self):
        if self.head is None:
            return "Stack Underflow"
        item = self.head.data
        self.head = self.head.next
        return item
    def length(self):
        if self.head is None:
            return 0
        else:
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.next
        return count
    def isEmpty(self):
        return self.length() == 0
    def display(self):
        if self.head is None:
            return "stack is empty"
        current = self.head
        print("Head ", end =" -> ")
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
        print("Tail")
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.display()
st.pop()
st.display()
print(st.isEmpty())
print(st.length())