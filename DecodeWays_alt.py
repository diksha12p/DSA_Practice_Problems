class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        return self._dp_helper(s, dp)

    def _dp_helper(self, data, dp):
        # Base Case 1: Empty string
        if not data:
            return 1

        first_call, second_call = 0, 0

        if data in dp:
            return dp[data]

        if 1 <= int(data[:1]) <= 9:
            first_call = self._dp_helper(data[1:], dp)

        if 10 <= int(data[:2]) <= 26:
            second_call = self._dp_helper(data[2:], dp)

        dp[data] = first_call + second_call

        return dp[data]

    def _rec_helper(self, data):
        # Base Case 1: Empty string
        if not data:
            return 1

        first_call, second_call = 0, 0

        if 1 <= int(data[:1]) <= 9:
            first_call = self._rec_helper(data[1:])

        if 10 <= int(data[:2]) <= 26:
            second_call = self._rec_helper(data[2:])

        return first_call + second_call


sol = Solution()
print(sol.numDecodings("12"))
