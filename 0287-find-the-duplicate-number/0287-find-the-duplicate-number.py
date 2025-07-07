class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqiency = set()
        for num in nums:
            if num in freqiency:
                return num
            freqiency.add(num)