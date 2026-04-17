class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtracking(start, end, curr ):
            if len(curr) == n*2:
                ans.append(curr[:])
            
            if start < n:
                backtracking(start +1, end, curr + "(")
            if end < start:
                backtracking(start, end +1, curr + ")" )

        backtracking(0, 0, "")
        return ans

# 2 * 2 * 2 *  2 * 2 * 2 = 2 ^ n*2