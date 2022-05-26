class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        new_range = max(arr) + k + 1
        missing_num = [num for num in range(new_range) if num not in arr]
        return missing_num[k]