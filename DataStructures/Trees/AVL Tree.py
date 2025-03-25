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


avl = AVLTree()

# Test 1: LL Imbalance
for val in [30, 20, 10]:
    avl.insert_value(val)

print("Inorder Traversal after LL Rotation:")
avl.inorder_traversal(avl.root)
print("\n")


