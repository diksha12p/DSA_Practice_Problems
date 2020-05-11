class Solution:
    def findJudge(self, N: int, trust) -> int:
        candidates = [False for _ in range(N)]
        for entry in trust:
            candidates[entry[0] - 1] = True

        for i,x in enumerate(candidates):
            if not x:
                return i+1
        return -1

        # judge = [i for i, x in enumerate(candidates) if not x else -1][0]
        # return judge


sol = Solution()
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(sol.findJudge(N, trust))



