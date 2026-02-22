class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [-1,0],[0,-1]]

        res = 0

        def dfs(i,j):
            
            grid[i][j] = 0
            area = 1

            for dx, dy in dirs:
                x, y = i+dx, j+dy

                if 0<= x<m and 0<=y<n and grid[x][y]==1:
                    area += dfs(x,y)
            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 :
                    a = dfs(r,c)
                    res = max(res, a)
        return res

































