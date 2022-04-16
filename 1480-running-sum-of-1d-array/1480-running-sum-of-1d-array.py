class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = [nums[0]]
        for num in range(1, len(nums)) : 
            new_list.append(nums[num] + new_list[num -1])
        return new_list