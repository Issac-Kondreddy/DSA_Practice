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

    def delete(self, value):
        if self.root is None:
            return "Tree is Empty"

        parent = None
        current = self.root
        while current:
            if value < current.data:
                parent = current
                current = current.left
            elif value > current.data:
                parent = current
                current = current.right
            else:
                # Case 1: No child (leaf node)
                if not current.left and not current.right:
                    if parent:
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        self.root = None
                    return f"Leaf Node {value} deleted"

                # Case 2: One child
                elif current.left and not current.right:
                    if parent:
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    else:
                        self.root = current.left
                    return f"Node {value} with one child deleted"
                elif current.right and not current.left:
                    if parent:
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    else:
                        self.root = current.right
                    return f"Node {value} with one child deleted"

                # Case 3: Two children
                elif current.left and current.right:
                    successor_parent = current
                    successor = current.right
                    while successor.left:
                        successor_parent = successor
                        successor = successor.left
                    # Replace data
                    current.data = successor.data
                    # Remove the successor
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                    return f"Node {value} deleted and replaced with successor {successor.data}"
                break
        return "Node Not Found"

    # Testing the tree and methods
BST = BinarySearchTree()
print(BST.insert(20))
print(BST.insert(10))
print(BST.insert(25))
print(BST.insert(12))
print(BST.insert(18))
BST.inorder(BST.root)
print("\n")
BST.search(12)
print(BST.delete(12))
BST.inorder(BST.root)
BST.inorder(BST.root)