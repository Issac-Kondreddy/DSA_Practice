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
                current = queue.pop(0)
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
    #Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end= " ")
            self.inorder(root.right)
    #PreOrder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)
     #post order
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")



bt = BinaryTree()
print(bt.insert(1))
print(bt.insert(2))
print(bt.insert(3))
print(bt.insert(4))
print("In Order Traversal : ")
bt.inorder(bt.root)
print()
print("Pre Order Traversal : ")
bt.preorder(bt.root)
print()
print("Post Order Traversal : ")
bt.postorder(bt.root)