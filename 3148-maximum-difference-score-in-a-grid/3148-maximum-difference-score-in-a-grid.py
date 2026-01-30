class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i,j):
            if i >= m or j >= n:
                return 0 

            max_val = float("-inf")

            if i+1 < m:
                max_val = max(max_val,grid[i+1][j]-grid[i][j]+dfs(i+1,j))

            if j+1 < n:
                max_val = max(max_val,grid[i][j+1]-grid[i][j]+dfs(i,j+1))

            return max(0,max_val)

        mx_val, mx_val1 = float("-inf"), float("-inf")

        for i in range(m):
            for j in range(n):
                mx_val = max(mx_val,dfs(i,j))
                if (i+1 < m):
                    mx_val1 = max(mx_val1,grid[i+1][j]-grid[i][j])
                if (j+1 < n):
                    mx_val1 = max(mx_val1,grid[i][j+1]-grid[i][j])

        if mx_val == 0:
            return mx_val1

        return mx_val 



        