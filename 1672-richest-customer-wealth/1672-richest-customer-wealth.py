class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = max(sum(i) for i in accounts)
        return max_num