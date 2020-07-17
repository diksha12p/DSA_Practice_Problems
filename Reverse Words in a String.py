class Solution:
    def reverseWords_alt(self, s: str) -> str:
        return ' '.join(list(s.lstrip().rstrip().split())[::-1])

    def reverseWords(self, s: str) -> str:
        def rev(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            # print("Output of 'rev' call --  ", s)
            return

        def rev_words(s):
            i = 0
            while i < len(s):
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    break
                # s[i] starts a word, now find j that ends a word
                j = i
                while j + 1 < len(s) and s[j + 1] != ' ':
                    j += 1
                # s[j] ends a word
                rev(s, i, j)
                i = j + 1
            # print("Output of 'rev_words call -- ", s)

        def trim(s):
            i, j = 0, 0  # j to be checked, i holds index of next chr
            for j in range(len(s)):
                if s[j] != ' ':
                    if i > 0 and j > 0 and s[j - 1] == ' ':  # this is key, to determine if we need add a space or not.
                        s[i] = ' '
                        i += 1
                    s[i] = s[j]
                    i += 1
            return s[:i]

        sentence = list(s)
        rev(sentence, 0, len(sentence) - 1)
        rev_words(sentence)
        arr = trim(sentence)
        # print(arr)
        return ''.join(arr)


if __name__ == '__main__':
    sol = Solution()
    sentence = "  hello world!  "
    print(sol.reverseWords(sentence))