class Solution:


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [(0,1), (1,0), (1,1)]

        max_area = 0
        memo = {}

        def dfs(r,c):
            nonlocal max_area
            if r >= rows or c >= cols:
                return 0
            if (r,c) not in memo:
                side = float('inf')
                
                for dx, dy in dirs:
                    x,y = r+dx, c+dy
                    side = min(side, dfs(x,y))

                if matrix[r][c] == '1':
                    side += 1
                else:
                    side = 0
                max_area = max(max_area, side*side)
                memo[(r,c)] = side
            # print(f"max side at i,j : {r,c} = side : {side}")
            return memo[(r,c)]

        dfs(0,0)
        return max_area
        