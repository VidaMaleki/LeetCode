class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = sum(nums)
        str_nums = ""
        for i in nums:
            str_nums += str(i)
        digit_nums = 0
        for i in list(str_nums):
            digit_nums += int(i)
        print(el_sum, digit_nums)
        return el_sum - digit_nums