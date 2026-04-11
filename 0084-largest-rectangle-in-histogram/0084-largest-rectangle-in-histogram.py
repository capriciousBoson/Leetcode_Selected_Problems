class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smaller = [-1 for _ in range(n)]
        prev_smaller = [-1 for _ in range(n)]

        stk = [-1]
        for i, h in enumerate(heights):
            while stk[-1]!=-1 and heights[stk[-1]] >= h:
                stk.pop()
            prev_smaller[i] = stk[-1]
            stk.append(i)
        print(prev_smaller)

        stk = [n]
        for i in range(n-1, -1, -1):
            while stk[-1]!=n and heights[stk[-1]] >= heights[i]:
                stk.pop()
            next_smaller[i] = stk[-1]
            stk.append(i)

        print(next_smaller)

        res = heights[0]
        for i in range(n):
            width = next_smaller[i]-1 - prev_smaller[i]
            area = width*heights[i]
            res = max(res, area)
        return res
        


        