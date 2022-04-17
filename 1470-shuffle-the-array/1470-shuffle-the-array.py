class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        for x, y in zip(nums[:n],nums[n:]):
            new_list.append(x)
            new_list.append(y)
        return new_list