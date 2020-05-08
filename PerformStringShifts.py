class Solution:
    def stringShift(self, arr, shift):
        for entry in shift:
            i = entry[1]
            if entry[0] == 1:
                arr = arr[-i:] + arr[:-i]
            else:
                arr = arr[i:] + arr[:i]
        return arr

    def _net_shift(self, shift):
        # sum_right, sum_left = 0,0
        # for type,amount in shift:
        #     if type == 1:
        #         sum_right += amount
        #     else:
        #         sum_left += amount
        # return sum_right - sum_left
        return sum([x[1] if x[0] == 0 else -x[1] for x in shift])

    def string_shift(self, arr, shift):
        i = self._net_shift(shift) % len(arr)
        if i != 0:
            return arr[i:] + arr[:i]


sol= Solution()
s = "wphhcj"
shift = [[0,7],[0,3],[0,6],[1,7],[1,3],[1,2]]
print(sol.stringShift(s, shift))
print(sol.string_shift(s, shift))
