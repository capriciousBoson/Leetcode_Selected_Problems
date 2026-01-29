class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        def findPaths(i,j):
            if i>=rows or j>= cols:
                return 0
            elif obstacleGrid[i][j]==1:
                return 0
            elif i==rows-1 and j==cols-1:
                return 1
            
            if (i,j) not in memo:
                memo[(i,j)] = findPaths(i+1,j) + findPaths(i,j+1)
            return memo[(i,j)]
        
        return findPaths(0,0)
        