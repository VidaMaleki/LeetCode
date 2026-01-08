class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        candidates.sort()

        def backtracking(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                backtracking(i, curr, total + candidates[i])
                curr.pop()

        backtracking(0, [], 0)
        return res
        