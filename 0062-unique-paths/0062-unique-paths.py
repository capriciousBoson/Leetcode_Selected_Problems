class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def findPaths(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i >= m or j >=n:
                return 0
            
            if (i,j) not in memo:
                memo[(i,j)] = findPaths(i+1,j) + findPaths(i,j+1)
            return memo[(i,j)]
            
        return findPaths(0,0)
            
