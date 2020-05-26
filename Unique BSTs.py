"""
LC 96: Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""


class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                # numTrees(3) = numTrees(0)*numTrees(2) + numTrees(1)*numTrees(1) + numTrees(2)*numTrees(0)
                res[i] += res[j] * res[i - 1 - j]
        return res[n]
