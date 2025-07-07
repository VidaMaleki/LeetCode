class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m ==0:
            nums1[:] = nums2
            return nums1
        if n == 0:
            return nums1
        index_1 = m-1
        index_2 = n-1
        k = m+n-1

        while index_1 >=0 and index_2>=0:
            if nums1[index_1]> nums2[index_2]:
                nums1[k] = nums1[index_1]
                index_1 -=1
                
            else:
                nums1[k] = nums2[index_2]
                index_2 -=1
            k -=1
        while index_2 >=0:
            nums1[k] = nums2[index_2]
            index_2 -=1
            k-=1
        
        return nums1
        
        