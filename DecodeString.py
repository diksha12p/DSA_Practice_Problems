class Solution:
    def decodeString(self, s):
        if not s:
            return ""
        stack = []

        for char in s:
            if char.isalpha() or char.isdigit() or char == "[":
                stack.append(char)
            elif char == "]":
                sub_string = ""
                while stack[-1] != "[":
                    sub_string += stack.pop()
                stack.pop()

                times = ""
                while stack and stack[-1].isdigit():
                    times += stack.pop()

                stack.append(sub_string * int(times))

        return "".join(stack)


sol = Solution()
string = "3[a2[c]]"
print(sol.decodeString(string))
