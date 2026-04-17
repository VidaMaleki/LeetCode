class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [73,74,75,71,69,72,76,73]
        stack = []
        ans = 
        """
        stack = [] # 73
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1): #n
            while stack and temperatures[stack[-1]] <= temperatures[i]: 
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            else:
                ans[i] = 0

            stack.append(i)
        return ans