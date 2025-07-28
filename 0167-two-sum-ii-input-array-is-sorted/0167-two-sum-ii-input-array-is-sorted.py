class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in num_map:
                return [num_map[diff]+ 1, i +1]
            num_map[num] = i
            