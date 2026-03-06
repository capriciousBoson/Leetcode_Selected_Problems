class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights) 

        stk = [-1]
        for i in range(n):
            while stk[-1]!=-1 and heights[stk[-1]] >= heights[i]:
                idx = stk.pop()
                ps = stk[-1] 
                ns = i
                area = heights[idx]*(ns-ps-1)
                res = max(res, area)
            stk.append(i)
        
        while stk:
            idx = stk.pop()
            if idx == -1: break
            ns = n
            ps = stk[-1]
            area = heights[idx]*(ns-ps-1)
            res = max(res, area)
        return res

                

        # ns = [-1 for n in heights]
        # # ps = [-1 for n in heights]
        # res = 0

        # n = len(heights)
        # stk = [n]
        # for i in range(n-1, -1, -1):
        #     while stk[-1]!=n and heights[stk[-1]] >= heights[i]:
        #         stk.pop()
        #     ns[i] = stk[-1]
        #     stk.append(i)
        
        # stk = [-1]
        # for i in range(n):
        #     while stk[-1]!=-1 and heights[stk[-1]] >= heights[i]:
        #         stk.pop()
        #     ps_i = stk[-1]
        #     stk.append(i)

        #     # calculate area for current height
        #     area = heights[i]*(ns[i]-ps_i-1)
        #     res = max(res, area)

        # return res
        