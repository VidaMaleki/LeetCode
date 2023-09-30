class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Input: nums = [4,5,2,1], queries = [3,10,21]
        # Output: [2,3,4]
        nums.sort() # Out put will sort nums [1, 2, 4, 5]
        answer = []
        for num in queries: # first loop num = 5 
            left = 0 # left = 3 
            right = len(nums) # 3
            # if num < nums[0]:
            #     answer.append(0)
            # elif nums[0] <= num:
            #     answer.append(1)
            # elif(num >= nums[right-1]):
            #     answer.append(len(nums))
            # else:        
            while left < right: 
                mid = (left + right) // 2 # mid = 2

                if sum(nums[:mid+1]) <= num: # 7 <= 10
                    left = mid + 1
                else:
                    right = mid 
            answer.append(left) #2 , 3, 
        return answer