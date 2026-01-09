class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        index = 0
        ans = []
        while index < len(nums):
            ans.append(nums[left])
            ans.append(nums[right])
            left+=1
            right+=1
            index+=2
        return ans