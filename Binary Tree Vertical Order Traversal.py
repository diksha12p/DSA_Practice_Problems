"""
987. Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at
positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
"""
from typing import List
from collections import defaultdict


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: Node) -> List[List[int]]:
        d = defaultdict(list)
        self._node_pos(0,0, root, d)
        return [[value[1] for value in sorted(d[key])] for key in sorted(d)]

    def _node_pos(self, X, Y, root, d):
        if not root:
            return
        d[X].append((Y, root.val))
        self._node_pos(X-1, Y+1, root.left, d)
        self._node_pos(X + 1, Y + 1, root.right, d)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

sol = Solution()
print(sol.verticalTraversal(root))

