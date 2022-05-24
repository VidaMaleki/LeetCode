class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums = []
        new_range = max(arr) + k + 1

        for i in range(new_range):
            if i not in arr:
                missing_nums.append(i)
        return missing_nums[k]