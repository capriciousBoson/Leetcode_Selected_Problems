class Solution:
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
            # print(f"at i :{i} | current_heights : {current_heights}")

            stk = [-1]
            for idx in range(cols):
                while stk[-1]!=-1 and current_heights[stk[-1]] >= current_heights[idx]:
                    p = stk.pop()
                    pse = stk[-1]
                    nse = idx
                    # print(f"for idx :{p} pse : {pse}, nse : {nse}")
                    area = (nse-pse-1)*current_heights[p]
                    # print(f"calculated area : {area}")
                    max_area = max(max_area, area)
                stk.append(idx)

            while stk:
                i2 = stk.pop()
                if i2==-1: break
                pse = stk[-1]
                nse = cols
                area = (nse-pse-1)*current_heights[i2]
                # print(f"for idx : {i2}, pse : {pse} and nse : {nse} , area : {area}")
                max_area = max(max_area, area)

        return max_area
            

        