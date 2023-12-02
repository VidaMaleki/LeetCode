class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        current = float('-inf')
        while current != target:
            current = numbers[left] + numbers[right]
            print(current)
            print(left, right)
            if current > target:
                right -=1
            elif current < target:
                left +=1
            else:
                return [left +1, right +1]
            
        