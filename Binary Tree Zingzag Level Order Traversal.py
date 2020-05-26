"""
LC 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""
from typing import List


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        flag, result = 1, []
        while queue:
            list_entry = list()
            if flag == -1:
                result.append([node.val for node in queue[::-1] if node is not None ])
            else:
                result.append([node.val for node in queue if node is not None])
            flag *= -1

            for node in queue:
                if node.left: list_entry.append(node.left)
                if node.right: list_entry.append(node.right)
            queue = list_entry
        return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
# root.left.left = Node(7)
# root.left.right = Node(6)
root.right.left = Node(15)
root.right.right = Node(7)

sol = Solution()
print(sol.zigzagLevelOrder(root))