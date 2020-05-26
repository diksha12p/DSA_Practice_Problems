class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # In order traversal
        if not root:
            return
        queue = []
        while queue:
            node = queue.pop[0]
            flag = False

            if node.left:
                if flag: return False
                queue.append(node.left)
            else:
                flag = True

            if node.right:
                if flag: return False
                queue.append(node.right)
            else:
                flag = True

        return False










sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

print(sol.isCompleteTree(root))


