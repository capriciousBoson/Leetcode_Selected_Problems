class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return 0
        rows,cols = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (-1,0), (0, -1)]

        safety = [[float('inf') for _ in range(cols)] for __ in range(rows)]
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    q.append((i,j, 0))
        
        # print(f"1s  : {q}")

        while q:
            x,y, s = q.popleft()
            if safety[x][y] != float('inf'):
                continue
            safety[x][y] = s


            for dx,dy in dirs:
                x2,y2 = dx+x, dy+y
                if 0<=x2<rows and 0<=y2<cols and safety[x2][y2]>s+1:
                    q.append((x2,y2, s+1))

        # for r_ in safety:
        #     print(r_)
        heap = [(-safety[0][0], 0,0 )]
        
        visited = [[0 for _ in range(cols)] for __ in range(rows)]
        while heap:
            s, i,j  = heapq.heappop(heap)
            s *= -1

            if i==rows-1 and j==cols-1:
                return s

            if visited[i][j]:
                continue

            visited[i][j] = 1

            
            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<rows and 0<=y<cols and not visited[x][y]:
                    heapq.heappush(heap, (-min(safety[x][y], s), x, y))
        return 0

        
        