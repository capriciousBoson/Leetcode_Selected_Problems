class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def bfs(Q, visited):
            while Q:
                i_, j_, prev_height = Q.popleft()
                visited.add((i_,j_))
                
                for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    x, y = i_ + dx,  j_ + dy
                    if 0<=x<m and 0<=y<n and heights[x][y] >= prev_height and (x,y) not in visited:
                        Q.append((x,y, heights[x][y]))
                        # visited.add((x,y))
        
        Q_pac = collections.deque()
        Q_atl = collections.deque()
        for j in range(n):
            Q_pac.append((0,j, heights[0][j]))
            # pac.add((0,j))
            Q_atl.append((m-1, j, heights[m-1][j]))
            # atl.add((m-1,j))
        for i in range(m):
            Q_pac.append((i, 0, heights[i][0]))
            # pac.add((i,0))
            Q_atl.append((i, n-1, heights[i][n-1]))
            # atl.add((i, n-1))
        
        bfs(Q_pac, pac)
        bfs(Q_atl, atl)
        res = []

        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res


        



        