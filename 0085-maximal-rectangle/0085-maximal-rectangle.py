class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        best = 0

        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            stack = []
            for j in range(n + 1):
                h = heights[j] if j < n else 0
                while stack and heights[stack[-1]] >= h:
                    height = heights[stack.pop()]
                    left = stack[-1] + 1 if stack else 0
                    best = max(best, height * (j - left))
                stack.append(j)

        return best
        