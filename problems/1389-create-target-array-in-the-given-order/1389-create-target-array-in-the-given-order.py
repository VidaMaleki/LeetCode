class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        target_loop = [target.insert(i, number) for number, i in zip(nums, index) ]
        return target