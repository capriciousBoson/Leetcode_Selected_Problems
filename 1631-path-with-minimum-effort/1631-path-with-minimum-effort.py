class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
        r,c = len(heights), len(heights[0])

        min_efforts = [[float('inf') for _ in range(c)] for __ in range(r)]

        pq = [[0,0,0]]

        while pq:
            effort, i,j = heapq.heappop(pq)
            if i==r-1 and j==c-1:
                return effort
            
            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<r and 0<=y<c:
                    new_effort = max(effort, abs(heights[i][j] - heights[x][y]))
                    if new_effort < min_efforts[x][y]:
                        min_efforts[x][y] = new_effort
                        heapq.heappush(pq, [new_effort, x, y])

        return min_efforts[r-1][c-1]

