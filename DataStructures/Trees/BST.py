class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return f"Node Inserted as root node {self.root.data}"
        else:
            current = self.root
            while True:
                if value < current.data:
                    if current.left is None:
                        current.left = newnode
                        return f"Node Inserted at left of {current.data}"
                    else:
                        current = current.left
                if value > current.data:
                    if current.right is None:
                        current.right = newnode
                        return f"Node Inserted at right of {current.data}"
                    else:
                        current = current.right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data,end = " ")
            self.inorder(root.right)

    def search(self, value):
        if self.root is None:
            return "Tree is empty"
        else:
            if self.root.data == value:
                return f"Node found at root {value}"
            current = self.root
            depth = 0
            while current:
                if current.data < value:
                    current = current.right
                    depth += 1
                if current.data > value:
                    current = current.left
                    depth += 1
                if current.data == value:
                    print(f"Node {value} Found at depth {depth}")
                    return
            print(f"Node {value} not found")

BST = BinarySearchTree()
print(BST.insert(20))
print(BST.insert(10))
print(BST.insert(25))
print(BST.insert(12))
print(BST.insert(18))
BST.inorder(BST.root)
print()
BST.search(12)