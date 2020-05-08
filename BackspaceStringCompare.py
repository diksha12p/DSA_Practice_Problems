class Solution:

    def backspace_compare(self, str1, str2):
        str1, str2 = self._helper(str1), self._helper(str2)
        return str1 == str2

    def _helper(self, s):
        # while "#" in s:
        #     i = s.index("#")
        #     s = s[:i-1] + s[i+1:] if i >0 else s[i+1:]
        # return s
        stack = []
        for ele in s:
            # if ele != "#":
            #     stack.append(ele)
            # elif stack:
            #     stack.pop()
            if stack:
                stack.append(ele) if ele != "#" else stack.pop
        return stack




S = "a##c"
T = "#a#c"
sol = Solution()
print(sol.backspace_compare(S , T))