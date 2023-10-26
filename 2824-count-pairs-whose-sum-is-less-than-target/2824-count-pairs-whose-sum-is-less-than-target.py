class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i = 0
        j = 1
        answer = 0
        while i < len(nums)-1:
            print("i", i,"j", j ,"answer",answer )
            if (i < j) and (nums[i] + nums[j] < target):
                answer +=1
            if j == len(nums) -1:
                j = i + 1
                i +=1
                
            j+=1 
        return answer