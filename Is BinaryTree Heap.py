"""
https://leetcode.com/playground/ggCP5KTt
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_complete(self, root: TreeNode) -> bool:
        if not root: return
        queue = [root]
        while queue:
            node = queue.pop(0)
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
        return True

    def heap_util(self, root):
        if not root.left and not root.right:
            return True
        if not root.right:
            return root.left.val >= root.val
        else:
            if root.left.val >= root.val and root.right.val >= root.val:
                return self.heap_util(root.left) and self.heap_util(root.right)
            else:
                return False

    def is_heap(self, root):
        return self.heap_util(root) and self.is_complete(root)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)

    print(sol.is_heap(root))


