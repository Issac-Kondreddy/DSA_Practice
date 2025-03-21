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


    #Search using DFS
    def dfssearch(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return True
        left_res = self.dfssearch(root.left, value)
        right_res = self.dfssearch(root.right, value)
        return left_res or right_res

    def bfssearch(self, root, value):
        if root is None:
            return False
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.data == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    #Deletion
    def delete(self, value):
        if self.root is None:
            return "Tree is Empty"

        #first find the value to be deleted
        queue = [self.root]
        target_node = None
        while queue:
            current = queue.pop(0)
            if current.data ==value:
                target_node = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        if not target_node:
            return "Node not Found"

        #find the deepest Node
        deepestNode = None
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            deepestNode = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        #swap the deepestnode value to targetnode
        target_node.data, deepestNode.data = deepestNode.data, target_node.data

        #remove the deepestNode
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left == deepestNode:
                current.left = None
                return f"Node {value} deleted"
            if current.right == deepestNode:
                current.right = None
                return f"Node {value} deleted"

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)



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
print(bt.dfssearch(bt.root, 3))
print(bt.bfssearch(bt.root, 3))
bt.delete(3)
bt.postorder(bt.root)