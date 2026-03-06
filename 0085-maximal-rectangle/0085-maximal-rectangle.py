class Solution:
    def largestRectangleArea(self, heights):
        stk = [-1]
        maximum_area = 0
        for idx in range(len(heights)):
            while stk[-1]!=-1 and heights[stk[-1]] >= heights[idx]:
                p = stk.pop()
                pse = stk[-1]
                nse = idx
                # print(f"for idx :{p} pse : {pse}, nse : {nse}")
                area = (nse-pse-1)*heights[p]
                # print(f"calculated area : {area}")
                maximum_area = max(maximum_area, area)
            stk.append(idx)

        while stk:
            i2 = stk.pop()
            if i2==-1: break
            pse = stk[-1]
            nse = len(heights)
            area = (nse-pse-1)*heights[i2]
            # print(f"for idx : {i2}, pse : {pse} and nse : {nse} , area : {area}")
            maximum_area = max(maximum_area, area)
        return maximum_area


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        current_heights = [0 for _ in range(cols)]


        max_area = 0

        for i in range(rows):
            # print(f"\nat row : {i}")
            # update current heights
            for j in range(cols):
                # print(f"\ni,j : {i,j} | matrix[{i}][{j}] = {matrix[i][j]}")
                if matrix[i][j] == "1":
                    current_heights[j] += 1
                else:
                    current_heights[j] = 0
            
            # max_area = max(max_area, max(current_heights))
            # print(f"max_area : {max_area}")
            # use monotonic stk to find nest smaller element 
            #  and previous smaller element and find area
            max_area = max(max_area, self.largestRectangleArea(current_heights))

            

        return max_area
            

        