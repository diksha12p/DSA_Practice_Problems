# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0

        def helper(node: TreeNode):
            if node and not node.val % 2:
                if node.left:
                    if node.left.left:
                        self.total += node.left.left.val
                    if node.left.right:
                        self.total += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.total += node.right.left.val
                    if node.right.right:
                        self.total += node.right.right.val

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            return

        helper(root)
        return self.total





