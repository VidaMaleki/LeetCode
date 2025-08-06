class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        p = 0
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        for city in range(n):
            if city not in seen:
                seen.add(city)
                dfs(city)
                p +=1
        return p