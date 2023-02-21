class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 1
        # return sorted(x*x for x in A)
        # 2
        # square_list = []
        # for num in nums:
        #     square = num * num
        #     square_list.append(square)
        # return sorted(square_list)
        
        sorted_squares = [None] * len(nums)
        right = 0
        left = len(nums) -1
        n = len(nums) -1
        for i in range(len(nums)-1, -1, -1):
            print(i, nums[i], nums[right], nums[left])
            if abs(nums[right]) < abs(nums[left]):
                sorted_squares[i] = nums[left] ** 2
                left -=1
            else:
                sorted_squares[i] = nums[right] ** 2
                right +=1
        return sorted_squares
                
        