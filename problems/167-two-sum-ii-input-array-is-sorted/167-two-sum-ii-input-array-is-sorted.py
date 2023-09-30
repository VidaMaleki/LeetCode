class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        required = {}
        for i , num in enumerate(numbers):
            if target - num in required:
                return required[target - num]+1,i + 1
            else:
                required[num]=i
       
        