class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return f"Node Inserted {value}"
        else:
            queue = [self.root]
            while queue:
                current = queue.pop()
                if current.left is None:
                    current.left = newnode
                    return f"Node Inserted {value}"
                else:
                    queue.append(current.left)
                if current.right is None:
                    current.right = newnode
                    return f"Node Inserted {value}"
                else:
                    queue.append(current.right)

bt = BinaryTree()
print(bt.insert(1))
print(bt.insert(2))
print(bt.insert(3))
print(bt.insert(4))
