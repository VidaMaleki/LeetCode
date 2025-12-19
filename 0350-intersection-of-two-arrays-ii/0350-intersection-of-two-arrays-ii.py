class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_map = {}
        for num in nums1:
            nums_map[num] = nums_map.get(num, 0) +1
        ans = []
        for num in nums2:
            if num in nums_map and nums_map[num] != 0:
                nums_map[num] -=1
                ans.append(num)
        return ans
                

            
            