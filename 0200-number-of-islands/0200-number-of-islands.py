class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[False for _ in range(n)] for __ in range(m)]
        res  = 0
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                # print(f"\ngrid[{i}][{j}] : {grid[i][j]} | visited : {visited[i][j]}")
                if grid[i][j]=="1" and visited[i][j]==False:
                    res += 1
                    # print(f" updated res : {res}")

                    Q = collections.deque()
                    Q.append((i,j))
                    visited[i][j] = True

                    while Q:
                        i_, j_ = Q.popleft()
                        for dx, dy in dirs:
                            x,y = i_ + dx, j_ + dy
                            if 0<=x<m and 0<=y<n and grid[x][y]=="1" and not visited[x][y]:
                                Q.append((x,y))
                                visited[x][y] = True

                
        return res



        