class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        results = [0] * n
        stack = [] # pair of temp, index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                results[stackIndex] = (i - stackIndex)

            stack.append([temp, i])

        return results    
        