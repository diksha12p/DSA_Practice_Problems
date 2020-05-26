"""
Given a Binary Tree, write a function to check whether the given Binary Tree is a prefect Binary Tree or not.

Perfect Binary Tree -> Complete + Full
"""


class newNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


class Solution:
    def is_perfect(self, root):
        return self.is_full(root) and self.is_complete(root)

    def is_full(self,root):
        if root is None:
            return True
        if not root.left and not root.right:
            return True
        if root.left is not None and root.right is not None :
            return self.is_full(root.left) and self.is_full(root.right)
        return False

    def is_complete(self, root):
        if not root:
            return True
        queue, flag = [], False
        queue.append(root)
        while queue:
            node = queue.pop(0)
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


if __name__ == '__main__':
    # root = None
    root = newNode(10)
    root.left = newNode(20)
    root.right = newNode(30)

    root.left.left = newNode(40)
    root.left.right = newNode(50)
    root.right.left = newNode(60)
    # root.right.right = newNode(70)

    sol = Solution()
    print(sol.is_perfect(root))
