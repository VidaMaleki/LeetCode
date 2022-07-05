class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count[i] = count.get(i,0)+1
        single = None
        for key, value in count.items():
            if value == 1:
                single = key
        return single