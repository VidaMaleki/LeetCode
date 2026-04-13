class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [100,4,200,1,3,2]
        nums_set = set(nums)
        max_len = 0
        for num in nums_set: # o(n)
            if num -1 not in nums_set: # o(1)
                length = 1
                while num + length in nums_set: 
                    length+=1
                max_len = max(max_len, length)
        return max_len

        # time O(n + n)
        # space O(n)