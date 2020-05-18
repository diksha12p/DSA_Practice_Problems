class Solution(object):
    def calculate(self, s):
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)

            if c == '(':
                # find the corresponding ")"
                pCnt = 0
                end = 0
                clone = s[i:]
                while end < len(clone):
                    if clone[end] == '(':
                        pCnt += 1
                    elif clone[end] == ')':
                        pCnt -= 1
                        if pCnt == 0:
                            break
                    end += 1
                # do recursion to calculate the sum within the next (...)
                num = self.calculate(s[i + 1:i + end])
                i += end

            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / float(num))
                sign = c
                num = 0
            i += 1

        return sum(stack)



        # stack, sign, num = [], '+', 0
        # for i in range(len(s)):
        #     ch = s[i]
        #     if ch.isdigit():
        #         num = num*10+int(ch)
        #
        #     if ch == '(':
        #         p_count, curr_i = 0, 0
        #         clone = s[i:]
        #         while curr_i < len(clone):
        #             if clone[curr_i] == '(':
        #                 p_count += 1
        #             elif clone[curr_i] == ')':
        #                 p_count -= 1
        #
        #                 if p_count == 0:
        #                     break
        #             curr_i += 1
        #
        #         num = self.calculate(s[i+1:i+curr_i])
        #         i += curr_i
        #
        #     if (i + 1 == len(s)) or (ch == '+' or ch == '-' or ch == '*' or ch == '/'):
        #         if sign == '+':
        #             stack.append(num)
        #         elif sign == '-':
        #             stack.append(-num)
        #         elif sign == '*':
        #             stack[-1] = stack[-1] * num
        #         elif sign == '/':
        #             stack[-1] = int(stack[-1] / (num))
        #         sign = ch
        #         num = 0
        # return sum(stack)


arr = "2*(5+5*2)/3+(6/2+8)"
sol = Solution()
print(sol.calculate(arr))
