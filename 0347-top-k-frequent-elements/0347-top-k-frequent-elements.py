from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i, num in enumerate(nums):
            frequency[num] = frequency.get(num, 0) +1

        return heapq.nlargest(k, frequency.keys(), key=frequency.get)