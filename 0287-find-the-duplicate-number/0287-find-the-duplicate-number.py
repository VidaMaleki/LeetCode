class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_dict = {}
        for i in nums:
            if i in new_dict.keys():
                return i
            else:
                new_dict[i] = new_dict.get(i, 0) +1
        
        