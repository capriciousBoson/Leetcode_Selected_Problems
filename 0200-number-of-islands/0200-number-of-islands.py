class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # visited = [[False for _ in range(cols)] for __ in range(rows)]

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i,j):
            if grid[i][j]=='0':
                return

            grid[i][j] = '0'

            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<rows and 0<=y<cols and grid[x][y]=='1':
                    dfs(x,y)
            return
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' :
                    # print(f"\nnot visited r,c : {r,c}")
                    islands += 1
                    dfs(r,c)
                    # print(f"after visiting : ")
                    # for r_ in visited:
                        # print(r_)

        return islands
        


        