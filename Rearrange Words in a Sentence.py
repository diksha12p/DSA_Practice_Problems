class Solution:
    def arrangeWords(self, text: str) -> str:
        list_text = sorted(list(text.split()), key = len)
        # indices_count = [ele[0] for ele in sorted(enumerate(list_text), key=lambda x: len(x[1]))]
        return (''.join(i + " " for i in list_text)).capitalize().strip()


sol = Solution()
entry = "Leetcode is cool"
print(sol.arrangeWords(entry))