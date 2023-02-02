class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict={}
        for i in nums:
            nums_dict[i] = nums_dict.get(i,0)+1
            
        for k, v in nums_dict.items():
            if v > 1:
                return True
        return False