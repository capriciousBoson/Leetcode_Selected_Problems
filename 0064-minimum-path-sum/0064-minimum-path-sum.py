class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m,n = len(grid), len(grid[0])

        def pathSum(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            if i >= m or j >=n:
                return float('inf')

            if (i,j) not in memo:
                down = float('inf')
                right = float('inf')
                if i<m-1:
                    down = pathSum(i+1, j)
                if j < n-1:
                    right = pathSum(i, j+1)
                
                memo[(i,j)] = grid[i][j] + min(down, right)

            return memo[(i,j)]
        return pathSum(0,0)