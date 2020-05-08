class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

    def insert(self, root, node):
        if root is None:
            root = node
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)

    def min_in_order_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        # First locate the element to be deleted
        if root is None:
            return root
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else: # The Node to be deleted is the Root itself
            # One or No child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children
            new_root_node = self.min_in_order_value(root.right)
            root.value = new_root_node.value
            root.right = self.delete(root.right, new_root_node.value)
        return root

    def search(self, root, value_to_search):
        if root.value > value_to_search and root.left is not None:
            self.search(root.left, value_to_search)
        elif root.value < value_to_search and root.right is not None:
            self.search(root.right, value_to_search)
        elif root.value == value_to_search:
            print(str(root.value) + "   Is Found!")
        else:
            print(str(value_to_search) + "  Not Found !!")


arr = [10,15,5,6,7,8,89]
r = Node(arr[0])
for i in range(1, len(arr)):
    r.insert(r, Node(arr[i]))


r.inorder(r)

print("         ================================         ")
r.search(r, 78)

print("         ================================         ")
r.delete(r, 89)
r.inorder(r)








