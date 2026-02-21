class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix), len(matrix[0])

        dirs = [(0,1),(1,0), (0,-1), (-1,0)]
        memo = {}

        def dfs(i,j):
            if (i,j) not in memo:
                    
                res = 0
                for dx,dy  in dirs:
                    x,y  = i+dx, j+dy
                    if 0 <= x < r and 0<=y<c:
                        if matrix[x][y] > matrix[i][j]:
                            res = max(res, 1 + dfs(x,y))
                memo[(i,j)] = res
            return memo[(i,j)]
        
        ans = 0
        for a in range(r):
            for b in range(c):
                ans = max(ans, dfs(a,b))

        return ans + 1
        
        