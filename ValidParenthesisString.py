class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for i in s:
            if i == "(" or "*":
                count += 1
            elif i == ")":
                count += 1
            if count > 0:
                return False
        count = 0
        for i in s[::-1]:
            if i == ")" or "*":
                count -= 1
            elif i == "(":
                count += 1
            if count > 0:
                return False
        return True


sol = Solution()
string = "(*()"
print(sol.checkValidString(string))