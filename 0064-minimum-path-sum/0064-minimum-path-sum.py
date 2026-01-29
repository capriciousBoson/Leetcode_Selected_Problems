class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        memo = {}

        def pathSum(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            elif i >= m or j>= n:
                return float('inf')
            
            if (i,j) not in memo:
                memo[(i,j)] = grid[i][j] + min(pathSum(i+1,j), pathSum(i,j+1))
            return memo[(i,j)]
        return pathSum(0,0)
