class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = [nums[0]]
        for i in range(1,len(nums)):
            new_list.append(new_list[i-1]+ nums[i])
        return new_list