class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def can_split(max_sum: int) -> bool:
            pieces = 1
            curr = 0
            for x in nums:
                if curr + x <= max_sum:
                    curr += x
                else:
                    pieces += 1
                    curr = x
            return pieces <= k

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
        