class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ns = [-1 for n in heights]
        ps = [-1 for n in heights]

        n = len(heights)
        stk = [n]
        for i in range(n-1, -1, -1):
            while stk[-1]!=n and heights[stk[-1]] >= heights[i]:
                stk.pop()
            ns[i] = stk[-1]
            stk.append(i)
        
        stk = [-1]
        for i in range(n):
            while stk[-1]!=-1 and heights[stk[-1]] >= heights[i]:
                stk.pop()
            ps[i] = stk[-1]
            stk.append(i)
        
        res = 0
        for i in range(n):
            area = heights[i]*(ns[i]-ps[i]-1)
            res = max(res, area)
        return res
        