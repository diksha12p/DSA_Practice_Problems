class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root):
        result_list = []
        self.inorder(root, result_list)
        return min(b - a for a, b in zip(result_list, result_list[1:]))

    def inorder(self, node, result):
        if node.left: self.inorder(node.left, result)
        result.append(node.val)
        if node.right: self.inorder(node.right, result)

        return result


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    print(sol.getMinimumDifference(root))

