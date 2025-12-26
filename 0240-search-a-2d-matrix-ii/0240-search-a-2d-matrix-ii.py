from collections import defaultdict
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        i = 0
        j = n-1
        while i <=m-1 and j >= 0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j] > target:
                j -= 1
                continue
            elif matrix[i][j] < target:
                i += 1
                continue
        return False


            

        