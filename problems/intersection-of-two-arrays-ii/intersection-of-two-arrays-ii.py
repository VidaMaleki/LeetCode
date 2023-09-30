class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if(len(nums1)>len(nums2)):
        #     biggest_arr = nums1
        #     smallest_arr = nums2
        # else:
        #     biggest_arr = nums2
        #     smallest_arr = nums1
        
        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                nums2.remove(num)
        return intersection
    
    
        
        
        