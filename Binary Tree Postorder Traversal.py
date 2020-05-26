from typing import List

# Definition for a binary tree node.
"""
LC 145. Binary Tree Postorder Traversal
Both Iterative & Recursive
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative Implementation
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]

# #          Recursive Implementation
#         output = []
#         self._helper(root, output)
#         return output
#
#     def _helper(self, root, output):
#         if not root:
#             return
#         self._helper(root.left, output)
#         self._helper(root.right, output)
#         output.append(root.val)
#
