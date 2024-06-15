class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # List to store the left products
        list1 = [1] * n
        total = 1
        for i in range(n):
            list1[i] = total
            total *= nums[i]
        
        # List to store the right products
        list2 = [1] * n
        temp = 1
        for i in range(n-1, -1, -1):
            list2[i] = temp
            temp *= nums[i]
            
        result = [1] * n
        # Combine the left and right products to get the result
        for i in range(n):
            result[i] = list1[i] * list2[i]
        
        return result
        
          
            