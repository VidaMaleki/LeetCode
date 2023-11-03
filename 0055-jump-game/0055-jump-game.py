class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = nums[0]
        for i in range(1,len(nums)):
            print("steps first", steps)
            if steps == 0:
                return False
            steps -=1
            print("steps", steps, "i", i)
            steps = max(steps, nums[i])
        return True