class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        versions = [i for i in range(1,n+1)]
        versions = map(isBadVersion, versions)
        res = next((i for i, j in enumerate(versions) if j), None)
        return res




