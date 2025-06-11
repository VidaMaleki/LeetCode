class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6
        count 0 if count > k 
        start moving pointer left till count less than k
        every time we reach to k number of zero update answer with max
        
        """
        left = curr = ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr +=1
            while curr > k:
                if nums[left] == 0:
                    curr -=1
                left +=1
            
            ans = max(ans, i - left+1)
        return ans
        
                    
        