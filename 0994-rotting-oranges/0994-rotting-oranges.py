class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])

        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2 :
                    q.append((i,j, 0))
        min_minutes = 0

        while q:
            i,j, m = q.popleft()
            min_minutes = max(min_minutes, m)

            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<rows and 0<=y<cols and grid[x][y]==1:
                    grid[x][y] = 2
                    q.append((x,y, m+1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1


        return min_minutes