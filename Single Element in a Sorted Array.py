from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return nums[0]

        s, e = 0, ln - 1
        while s <= e:
            mid = (e - s) // 2 + s
            if (mid == 0 or nums[mid - 1] != nums[mid]) and (mid == ln - 1 or nums[mid + 1] != nums[mid]):
                return nums[mid]

            # total elements on left of mid including mid is (mid+1)
            # case 1: mid-1 == mid and elements on left including mid are even
            # case 2: mid+1 == mid and elements on left excluding mid are even
            # for case 1 and case 2: s = mid + 1 or s = mid + 2 (for case 2, mid == mid+1)
            # so can move to mid + 2
            if (mid == 0 or nums[mid - 1] == nums[mid]) and (mid + 1) % 2 == 0:
                s = mid + 1
            elif (mid == ln - 1 or nums[mid + 1] == nums[mid]) and (mid) % 2 == 0:
                s = mid + 2
            else:
                e = mid - 1

        return -1