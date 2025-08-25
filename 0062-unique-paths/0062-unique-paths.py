class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def fun(i,j):
            if i==m-1 and j==n-1:
                return 1
            elif i >= m or j>= n:
                return 0
            if (i,j) not in memo:
                down = 0
                right = 0
                if i<m-1:
                    down = fun(i+1,j)
                if j<n-1:
                    right = fun(i, j+1)
                memo[(i,j)] = down + right
            return memo[(i,j)]
        return fun(0,0)