class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums)-1:
            print("i", i)
            if nums[i-1] == nums[i]:
                print("nums[i-1]", nums[i-1], "nums[i]", nums[i])
                if nums[i+1] == nums[i]:
                    print("yes")
                    nums.remove(nums[i+1])
                else:
                    i+=1
            else:
                i +=1
        print("nums",nums)   
        return len(nums)