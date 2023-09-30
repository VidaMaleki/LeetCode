# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares(nums):
    squared_list = []
    left = 0
    right = len(nums)-1
    while left < right:
        max_right = nums[right] * nums[right] 
        max_left = nums[left] * nums[left]
        if (max_right) > (max_left):
            squared_list.insert(0,max_right)
            right -= 1
        else:
            squared_list.insert(0,max_left)
            left += 1
    print("left", left, "right", right)
    
    temp = nums[left] * nums[left]
    squared_list.insert(0, temp)
    
    return squared_list