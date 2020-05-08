class Solution:
    def lastStoneWeight(self, stones):
        if len(stones) == 1:
            return stones[0]
        else:
            while len(stones) >= 2:
                stones = self._helper(stones)
                if not stones:
                    return 0
            return stones[0]

    def _helper(self, arr):
        arr.sort()
        y, x = arr[-1], arr[-2]
        arr = arr[:-2]
        if y > x:
            arr.append(y - x)
            return arr
        else:
            return arr


sol = Solution()
stones = [2,2]
print(sol.lastStoneWeight(stones))