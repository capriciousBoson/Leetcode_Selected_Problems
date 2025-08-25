class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # memo = {}

        # def pathSum(i,j):
        #     if i==m-1 and j==n-1:
        #         return grid[i][j]
        #     if i >= m or j >=n:
        #         return float('inf')

        #     if (i,j) not in memo:
        #         down = float('inf')
        #         right = float('inf')
        #         if i<m-1:
        #             down = pathSum(i+1, j)
        #         if j < n-1:
        #             right = pathSum(i, j+1)
                
        #         memo[(i,j)] = grid[i][j] + min(down, right)

        #     return memo[(i,j)]
        # return pathSum(0,0)

        dp = [[float('inf') for _ in range(n+1)] for __ in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j==n-1 : continue
                # down = float('inf')
                # right = float('inf')

                # if i <m-1:
                #     down = dp[i+1][j]
                # if j < n-1:
                #     right = dp[i][j+1]
                down = dp[i+1][j]
                right = dp[i][j+1]
                
                dp[i][j] = grid[i][j] + min(down, right)
        return dp[0][0]
