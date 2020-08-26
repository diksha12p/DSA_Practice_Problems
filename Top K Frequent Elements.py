"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, _ in collections.Counter(nums).most_common(k)]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = [(-val, key) for key,val in collections.Counter(nums).items()]
        heapq.heapify(max_heap)
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result

    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        frequency, result = collections.Counter(nums), []
        inv_frequency = collections.defaultdict(list)
        # Filling up the buckets -> frequency to item mapping
        # frequency : List[List[int]]
        for key, freq in frequency.items():
            inv_frequency[freq].append(key)
        # Buckets will have frequency range from 0 to len(nums).
        # Thus, we find valid frequencies i.e. those with entries
        for i in range(len(nums), 0, -1):
            result.extend(inv_frequency[i])
            if len(result) >= k:
                break
        return result[:k]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]

    assert (sol.topKFrequent(nums, k=2)) == (sol.topKFrequent_heap(nums, k=2))
    assert (sol.topKFrequent(nums, k=2)) == (sol.topKFrequent_bucket(nums, k=2))

