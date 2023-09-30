class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_lists = sorted(nums1 + nums2)
        m1 = 0
        if len(merged_lists) % 2 == 0:
            m1 = len(merged_lists) // 2
            for i in range(len(merged_lists)):
                if i == m1:
                    return (merged_lists[i-1] + merged_lists[i]) / 2
        
        m1= len(merged_lists) // 2 
        for i in range(len(merged_lists)):
            if i == m1:
                return merged_lists[i]