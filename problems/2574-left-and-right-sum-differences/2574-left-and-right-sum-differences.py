class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_list= [0]
        right_list = [0]
        left = 0
        right = 0
        for i in range(len(nums)-1):
            left = sum(nums[:i+1])
            left_list.append(left)
        
        for i in range(len(nums)-1, 0, -1):
            right = sum(nums[-1: i-1:-1])
            right_list.insert(0, right)
        answer = []
        for i, j in zip(left_list, right_list):
            temp = abs(i - j)
            answer.append(temp)
        return answer