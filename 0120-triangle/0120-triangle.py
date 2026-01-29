class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        memo = {}

        def pathSum(r,i):
            if r==rows-1 and i<len(triangle[r]):
                return triangle[r][i]
            elif r>=rows or i >= len(triangle[r]):
                return float('inf')
            
            if (r,i) not in memo:
                memo[(r,i)] = triangle[r][i] + min(pathSum(r+1, i), pathSum(r+1, i+1))
            return memo[(r,i)]
        
        return pathSum(0,0)

        