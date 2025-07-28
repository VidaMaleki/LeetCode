class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) -1
        while i < n:
            sum_nums = numbers[i] + numbers[n]            
            if sum_nums < target:
                i +=1
            elif sum_nums > target:
                n -=1
            else:
                return [i+ 1, n +1]