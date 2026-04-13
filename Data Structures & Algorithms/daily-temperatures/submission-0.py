class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = []
        for i in range(n):
            tempCnt = 1

            j = i + 1 
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                tempCnt += 1
                j += 1

            if j == n:
                tempCnt = 0   

            results.append(tempCnt)

        return results 