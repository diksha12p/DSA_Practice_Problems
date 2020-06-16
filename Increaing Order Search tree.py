from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = self.inorder(root)
        head = TreeNode(result[0])
        current = head
        for i in range(1, len(result)):
            current.right = TreeNode(result[i])
            current = current.right
        return head

    def inorder(self, root: TreeNode) -> List:
        result, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result


