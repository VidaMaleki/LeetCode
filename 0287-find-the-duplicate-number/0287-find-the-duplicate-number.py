class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_dict = {}
        for i in nums:
            new_dict[i] = new_dict.get(i, 0) +1
        
        for i, j in new_dict.items():
            if j > 1:
                return i