"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
         1
       /  \
      2    3
     / \  /
    4  5 6

Output: 6
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Method 1: Basic Tree Traversal
    def countNodes_3(self, root: TreeNode) -> int:
        if not root: return 0
        count = 1
        if root.left:
            count += self.countNodes(root.left)
        if root.right:
            count += self.countNodes(root.right)

        return count

    # Method 2: Tree Traversal while using the properties of 'completeness' of a tree
    def countNodes_2(self, root: TreeNode) -> int:
        if root is None: return 0
        height_l, height_r, left_node, right_node = 0, 0, root, root

        while left_node is not None:
            height_l += 1
            left_node = left_node.left

        while right_node is not None:
            height_r += 1
            right_node = right_node.right

        if height_r == height_l:
            return (1 << height_r) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Method 3: Compare the heights of L and R subtrees. If equal => L subtree is full.
    # Thus, number of nodes is (2^height - 1). If unequal => R subtree is full.
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        height_l, height_r = self._heightLeft(root.left), self._heightLeft(root.right)
        if height_l == height_r:
            return (1 << height_l) + self.countNodes(root.right)
        else:
            return (1 << height_r) + self.countNodes(root.left)

    def _heightLeft(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height


if __name__ == '__main__':

    """
         1
       /  \
      2    3
     / \  /
    4  5 6
    
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    assert sol.countNodes(root) == 6, "Code Incorrect"
    assert sol.countNodes_2(root) == 6, "Code Incorrect"
    assert sol.countNodes_3(root) == 6, "Code Incorrect"
