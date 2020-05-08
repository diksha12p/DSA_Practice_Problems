class Solution:
    def reformat(self, s: str) -> str:
        digits = [char for char in s if char.isdigit()]
        alpha = [char for char in s if char.isalpha()]

        if abs(len(digits) - len(alpha)) > 1:
            return ""

        result = []
        start_with_alpha = len(alpha) > len(digits)
        while alpha or digits:
            result.append(alpha.pop() if start_with_alpha else digits.pop())
            start_with_alpha = not start_with_alpha

        return "".join(result)


sol = Solution()
string = "covid2019"
print(sol.reformat(string))
