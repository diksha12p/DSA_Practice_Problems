class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

            # Get the height of left and right sub-trees
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        # Get the diameter of left and irgh sub-trees
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)

        return max(lheight + rheight, max(ldiameter, rdiameter))

    def height(self, node):
        # Base Case : Tree is empty
        if node is None:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))


""" 
Constructed binary tree is  
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = Solution()

print(sol.diameterOfBinaryTree(root))


