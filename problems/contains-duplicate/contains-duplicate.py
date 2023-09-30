class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count= {}
        b=None
        for i, num in enumerate(nums):
            count[num] = count.get(num,0) +1
            if count[num] > 1:
                b=count[num]
        if b!= None:
            return True
        return False
                
        