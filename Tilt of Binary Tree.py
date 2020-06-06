"""
563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and
the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt = [0]
        self._helper(root, tilt)
        return tilt[0]

    def _helper(self, root, tilt):
        if not root:
            return 0
        left_sum = self._helper(root.left, tilt)
        right_sum = self._helper(root.right, tilt)

        tilt[0] += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum





