"""
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is
the sum of its values, divided by the number of nodes.

Example 1:

Input:
          20
	    /   \
	  12    18
    / | \   / \
  11  2  3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


class Solution:
    def __init__(self):
        self.result = [float('-inf'), 0]

    def max_avg(self, root: TreeNode):
        if not root or not root.children:
            return None

        self.dfs(root)
        return self.result[1]

    def dfs(self, root: TreeNode):
        if not root.children:
            self.result = [root.val, 1]

        curr_sum, curr_num = root.val, 1
        for child in root.children:
            child_sum, child_num = self.dfs(child)
            curr_sum += child_sum
            curr_num += child_num

        if curr_sum / curr_num > self.result[0]:
            self.result = [curr_sum / curr_num, root]

        return [curr_sum, curr_num]


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(20)
    root.children = [TreeNode(12), TreeNode(18)]
    root.children[0].children = [TreeNode(11), TreeNode(2), TreeNode(3)]
    root.children[1].children = [TreeNode(15), TreeNode(8)]

    ans = sol.max_avg(root)
    print(ans.val)



