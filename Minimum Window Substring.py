from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        dict_t = Counter(t)
        required = len(dict_t)
        l, r, curr_window, formed = 0, 0, {}, 0
        ans = float("inf"), None, None  # (len of window, left, right)

        while r < len(s):
            ch = s[r]
            curr_window[ch] = curr_window.get(ch, 0) + 1
            # Check if the frequency of 'ch' is same in both dictionaries
            if ch in dict_t and dict_t[ch] == curr_window[ch]:
                formed += 1
            # Once window is found, we contract to optimize this window
            while l <= r and formed == required:
                ch = s[l]
                # Update left and right pointers for 'ans' if we encounter a shorter window
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # Remove 'ch' from window -> contract it
                curr_window[ch] -= 1
                # Checking if the contraction led to removal of a valid ch
                if ch in dict_t and curr_window[ch] < dict_t[ch]:
                    formed -= 1
                # Move l by 1 to explore new window in either case
                l += 1
            # When done with contraction, expand the window
            r += 1
        return '' if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
