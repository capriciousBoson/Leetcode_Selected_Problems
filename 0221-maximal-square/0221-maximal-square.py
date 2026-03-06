class Solution:
    def largestSquareArea(self, heights):
        stk = [-1]
        maximum_area = 0
        for idx in range(len(heights)):
            while stk[-1]!=-1 and heights[stk[-1]] >= heights[idx]:
                p = stk.pop()
                pse = stk[-1]
                nse = idx
                side = min((nse-pse-1), heights[p] )
                maximum_area = max(maximum_area, side*side)
            stk.append(idx)

        while stk:
            i2 = stk.pop()
            if i2==-1: break
            pse = stk[-1]
            nse = len(heights)
            side = min((nse-pse-1), heights[i2] )
            maximum_area = max(maximum_area, side*side)

        return maximum_area


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        current_heights = [0 for _ in range(cols)]

        max_area = 0

        for i in range(rows):
            # update current heights
            for j in range(cols):
                if matrix[i][j] == "1":
                    current_heights[j] += 1
                else:
                    current_heights[j] = 0
  
            # use monotonic stk to find nest smaller element 
            #  and previous smaller element and find area

            max_area = max(max_area, self.largestSquareArea(current_heights))

            
        return max_area
        