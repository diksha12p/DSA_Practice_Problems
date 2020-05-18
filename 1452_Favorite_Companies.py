from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        i = 0
        result = []

        for i in range(len(favoriteCompanies)):

                if all(not set(favoriteCompanies[i]).issubset(favoriteCompanies[j]) for j in range(len(favoriteCompanies)) if j != i):
                    result.append(i)

        return result


sol = Solution()
arr = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(sol.peopleIndexes(arr))
