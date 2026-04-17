class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatMatrix = []

        for row in matrix:
            flatMatrix.extend(row)

        
        left = 0
        right = len(flatMatrix) -1
        print(flatMatrix)
        while left <= right:
            mid = left + (right-left) // 2
            print(mid)
            if flatMatrix[mid] == target: 
                return True

            elif flatMatrix[left] < target:
                left+=1
            else:
                right-=1
        
        return False