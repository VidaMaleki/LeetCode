class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) +1
        print(nums_dict)
        for k, v in nums_dict.items():
            print(k, v)
            if v > len(nums)/2:
                return k
        