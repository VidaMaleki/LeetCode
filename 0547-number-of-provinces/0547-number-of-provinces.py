from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] * n
        provinces = 0

        def dfs(city: int) -> None: 
            seen[city] = True 
            for nei in range(n): 
                if isConnected[city][nei] == 1 and not seen[nei]: 
                    dfs(nei) 
        for i in range(n): 
            if not seen[i]: 
                provinces += 1 
                dfs(i)

        return provinces