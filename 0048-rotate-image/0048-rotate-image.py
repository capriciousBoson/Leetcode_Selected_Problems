class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # top row - (i,j) - (j,n-1-i)
        # right col - (1,2) - (2, 1)
        #              0,2   - 2, 2
                        # 2,2 - 2,0
                        # 2,0 - 0,0
                        # 1,0 - 0, 1

                        # 0,0 - 0,2  (i,j) - (j, n-i)
                        # 0,2 - 2, 2  (j, n-i) - (n-i, n-j)
                        # 2,2 - 2,0    (n-i, n-j) - (n-j, i)
                        # 2,0 - 0,0    (n-j, i) - (i, j)
        n = len(matrix)-1
        j = 0
        while j <=n:
            for i in range(j, n-j):
               

                a = matrix[i][j]
                b = matrix[j][n-i]
                c = matrix[n-i][n-j]
                d = matrix[n-j][i]

                
                matrix[j][n-i] = a
                matrix[n-i][n-j] = b
                matrix[n-j][i] = c
                matrix[i][j] = d
            j += 1
        
         