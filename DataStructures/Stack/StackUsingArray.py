class Stack:

    def __init__(self):
        self.max_size = 10
        self.items = []
        self.top = -1
    def push(self, item):
        if self.top == self.max_size:
            return f"Stack Overflow"
        self.items.append(item)
        self.top += 1
        print(f"Item pushed {item}")
        return
    def pop(self):
        if self.top == -1:
            return "Stack Underflow"
        else:
            item = self.items.pop()
            print(f"Item popped {item}")
            self.top -= 1
    def peek(self):
        if self.top == -1:
            return "Stack is empty"
        else:
            return self.items[self.top]
    def isEmpty(self):
        return self.top == -1
    def display(self):
        print(self.items)
    def isFull(self):
        return self.top == self.max_size

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.peek())
print(stack.isFull())
stack.display()
print(stack.isEmpty())
stack.pop()
stack.display()

