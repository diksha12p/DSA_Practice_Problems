class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [None for _ in range(len(s) + 1)]
        return self._dp_helper(s, len(s), dp)
        # return self._rec_helper(s, len(s))

    # k : the last 'k' digits from the given number
    def _rec_helper(self, s, k):
        # Base Case 1: Input string is empty
        if k == 0 :
            return 1

        # Base Case 2: Input string starts with 0 i.e. there's no decoding
        start_i = len(s) - k
        if s[start_i] == '0':
            return 0

        result = self._rec_helper(s, k-1)
        if k >= 2 and int(s[start_i:start_i+2]) <= 26:
            result += self._rec_helper(s, k-2)
        return result

    def _dp_helper(self, s, k, dp):
        # Base Case 1: Input string is empty
        if k == 0 :
            return 1

        # Base Case 2: Input string starts with 0 i.e. there's no decoding
        start_i = len(s) - k
        if s[start_i] == '0':
            return 0

        if dp[k]:
            return dp[k]

        result = self._dp_helper(s, k-1, dp)
        if k >= 2 and int(s[start_i:start_i+2]) <= 26:
            result += self._dp_helper(s, k-2, dp)
        dp[k] = result
        return result


sol = Solution()
print(sol.numDecodings("12"))
