class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1, 1 , 2, 6
        24 12 4, 1
        24, 12, 8, 6

        1, -1, -1, 0, 0
        0   0  -9  3  1
        0. 0    9. 0.  0
        """
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
        

        