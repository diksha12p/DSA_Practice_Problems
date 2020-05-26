"""
LC # 144
Both Iterative and Recursive Implementations
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return result

#         output = []
#         self._helper(root, output)
#         return output

#     def _helper(self, root, output):
#         if root is None: return
#         output.append(root.val)
#         self._helper(root.left, output)
#         self._helper(root.right, output)

