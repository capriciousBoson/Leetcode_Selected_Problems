class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
        r,c = len(heights), len(heights[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        memo = {}

        def dfs(i,j, effort):
            if i==r-1 and j==c-1:
                return effort
            
            

            if (i,j,effort) not in visited:
                visited[i][j] = 1
                min_effort = float('inf')

                for dx, dy in dirs:
                    x,y = i+dx, j+dy
                    if 0<=x<r and 0<=y<c and not visited[x][y]:
                        effort_ = max(effort, abs(heights[i][j]-heights[x][y]))

                        new_effort = dfs(x,y, effort_)
                        min_effort = min(min_effort, new_effort)
                visited[i][j] = 0
                memo[(i,j,effort)] = min_effort
            return memo[(i,j,effort)]

        return dfs(0,0,0)
        