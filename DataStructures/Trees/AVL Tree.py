class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert_value(self, data):
        print(f"Inserting {data} into AVL Tree...")
        self.root = self.insert(self.root, data)

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if root.data > data:
            root.left = self.insert(root.left, data)
        elif root.data < data:
            root.right = self.insert(root.right, data)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if -1 <= balance <= 1:
            return root

        # Left Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Left Left Case
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)
        return root

    def search(self, root, key):
        if not root:
            return False
        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        """
                z
               /
              y
             / \
            x   T3
        """
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        return y

    def left_rotate(self,z):
        """
            z
             \
              y
             /  \
            T2   x
        """
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        return y

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"{root.data} (h={root.height})", end=" → ")
            self.inorder_traversal(root.right)
    def minval(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def delete_val(self, data):
        self.root = self.delete(self.root, data)
    def delete(self, root, key):
        if not root:
            return root
        if key<root.data:
            root.left = self.delete(root.left, key)
        elif key>root.data:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.minval(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


avl = AVLTree()

# Test 1: LL Imbalance
for val in [30, 20, 10, 40, 35]:
    avl.insert_value(val)

print("Root after insertions:", avl.root.data)
print("Inorder Traversal after insertions:")
avl.inorder_traversal(avl.root)
print("\n")

print("Deleting 10...")
avl.delete_val(10)
print("Inorder after deleting 10:")
avl.inorder_traversal(avl.root)
print("\n")

print("Deleting 30...")
avl.delete_val(30)
print("Inorder after deleting 30:")
avl.inorder_traversal(avl.root)
print("\n")

print("Searching for 35:", avl.search(avl.root, 35))  # True
print("Searching for 100:", avl.search(avl.root, 100))  # False



