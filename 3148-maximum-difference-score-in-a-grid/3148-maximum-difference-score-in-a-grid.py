class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # pad the grid with a top row  and left column consisting of float('inf')
        #  pad left
        grid = [[float('inf')] + row for row in grid]

        # pad top
        grid = [[float('inf') for _ in range(n+1)]] + grid
        # print(grid)
        res = -float('inf')
        # memo = {}

        for i in range(1,m+1):
            for j in range(1, n+1):

                x = min(grid[i-1][j], grid[i][j-1])
                # print(f"previous minimum at {i,j} = {x}")
                res = max(res, grid[i][j]-x)

                grid[i][j] = min(x, grid[i][j])
                # print(f"grid[{i}][{j}] = {grid[i][j]}")

        for r in grid:
            print(r)
        return res



            
        