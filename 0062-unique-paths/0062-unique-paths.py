class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}

        # def fun(i,j):
        #     if i==m-1 and j==n-1:
        #         return 1
        #     elif i >= m or j>= n:
        #         return 0
        #     if (i,j) not in memo:
        #         down = 0
        #         right = 0
        #         if i<m-1:
        #             down = fun(i+1,j)
        #         if j<n-1:
        #             right = fun(i, j+1)
        #         memo[(i,j)] = down + right
        #     return memo[(i,j)]
        # return fun(0,0)

        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue  # Already set to 1
                
                down = dp[i+1][j] if i+1 < m else 0
                right = dp[i][j+1] if j+1 < n else 0
                dp[i][j] = down + right
        return dp[0][0]
