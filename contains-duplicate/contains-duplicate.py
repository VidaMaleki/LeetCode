class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count= {}
        for i, num in enumerate(nums):
            count[num] = count.get(num,0) +1
        b=None
        for key, value in count.items():
            if value > 1 :
                b=value
        if b!= None:
            return True
        return False
                
        