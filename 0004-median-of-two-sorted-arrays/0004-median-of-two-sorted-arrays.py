class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        two_lists = nums1 + nums2
        print(two_lists)
        merged_lists = sorted(two_lists)
        print(merged_lists)
        m1 = 0
        if len(merged_lists) % 2 == 0:
            m1 = len(merged_lists) // 2
            print(m1)
            for i in range(len(merged_lists)):
                if i == m1:
                    return (merged_lists[i-1] + merged_lists[i]) / 2
        print(m1)
        
        m1= len(merged_lists) // 2 
        print(m1)
        for i in range(len(merged_lists)):
            if i == m1:
                return merged_lists[i]
        