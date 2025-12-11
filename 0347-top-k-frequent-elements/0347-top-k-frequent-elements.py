class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
           nums_map[num]  = nums_map.get(num, 0) +1
        
        
        sorted_freq = sorted(nums_map.items(), key=lambda x:x[1],reverse=True)
        # [(1, 3), (2, 2), (3, 1)]
        return [ k for k, v in sorted_freq[:k]]