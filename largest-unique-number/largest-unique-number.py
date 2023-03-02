class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) +1
        print(nums_dict)
      
        while len(nums_dict) > 0:
            max_num = max(nums_dict)
            if nums_dict[max_num] == 1:
                return max_num
            else:
                nums_dict.pop(max_num)
        
        return -1