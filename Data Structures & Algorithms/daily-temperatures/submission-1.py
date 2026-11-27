class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [1] * n
        stack = []
        for i in range(n):
            if not stack or temperatures[i] <= stack[-1][0]: 
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    idx = stack.pop()
                    results[idx[1]] = i - idx[1]
                stack.append((temperatures[i], i))
        while stack: 
            idx = stack.pop()
            results[idx[1]] = 0
        return results