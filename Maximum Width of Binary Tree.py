"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum
width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in
the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).


Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue, result = [[root, 0]], 1
        while len(queue):
            count, start, end = len(queue), queue[0][1], queue[-1][1]
            result = max(result, end - start + 1)
            for ch in range(count):
                curr = queue.pop(0)
                idx = curr[1] - start
                if curr[0].left:
                    queue.append([curr[0].left, 2 * idx + 1])
                if curr[0].right:
                    queue.append([curr[0].right, 2 * idx + 2])
        return result


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(4)

    assert (sol.widthOfBinaryTree(root)) == 3


