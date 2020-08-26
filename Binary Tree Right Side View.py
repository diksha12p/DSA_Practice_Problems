"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # IDEA 1: Level Order Traversal and append the ele at index = -1 to the final answer
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        # queue: List(TreeNode)
        result, queue = list(), [root]
        while queue:
            level = []
            result.append(queue[-1].val)
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
        return result

    # IDEA 2: Obtain the right side views for the left and right child of the root. (view_right, view_left)
    # Depending upon the length of view_right, append view_left[len(view_right) : ]
    def rightSideView_alt(self, root: TreeNode) -> List[int]:
        if not root: return []
        view_right = self.rightSideView_alt(root.right)
        view_left = self.rightSideView_alt(root.left)
        if len(view_left) < len(view_right):
            return [root.val] + view_right
        else:
            return [root.val] + view_right + view_left[len(view_right):]




