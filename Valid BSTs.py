"""
LC 98: Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = list()
        self._in_order(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False
        return True

    def _in_order(self, root: TreeNode, output: list) -> list:
        if root is None: return
        self._in_order(root.left, output)
        output.append(root.val)
        self._in_order(root.right, output)

#     def isValidBST(self, root: TreeNode) -> bool:
#         return self._in_order(root, [])

#     def _in_order(self, root : TreeNode, prev = []) -> bool:
#         if not root:
#             return True
#         if not self._in_order(root.left, prev):
#             return False

#         if not prev:
#             prev.append(root.val)
#         elif prev[0] >= root.val:
#             return False

#         prev[0] = root.val

#         if not self._in_order(root.right, prev):
#             return False

#         return True


