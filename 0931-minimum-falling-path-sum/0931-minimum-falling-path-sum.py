class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        memo = {}

        def pathSum(i,j):
            if i==m-1 and 0<=j<n:
                return matrix[i][j]
            elif i>=m or j>=n or j <0:
                return float('inf')
            
            if (i,j) not in memo:
                memo[(i,j)] = matrix[i][j] + min(
                                            pathSum(i+1,j-1), 
                                            pathSum(i+1,j),
                                            pathSum(i+1,j+1) )

            return memo[(i,j)]
        
        res = float('inf')
        for j in range(n):
            res = min(res, pathSum(0,j))

        return res
        