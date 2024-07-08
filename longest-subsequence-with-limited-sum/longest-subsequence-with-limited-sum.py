class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # nums = [4,5,2,1], queries = [3,10,21]
       
        sorted_nums = sorted(nums)
        prefix_sum = [sorted_nums[0]]
        for i in range(1, len(sorted_nums)):
            temp = prefix_sum[-1] + sorted_nums[i]
            prefix_sum.append(temp)
            
        def search(arr, target):
            left = 0
            right = len(arr) -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid -1
            return left
        
        max_sub = []
        for i in range(len(queries)):
            sub_arr = search(prefix_sum, queries[i])
            max_sub.append(sub_arr)
        return max_sub
            