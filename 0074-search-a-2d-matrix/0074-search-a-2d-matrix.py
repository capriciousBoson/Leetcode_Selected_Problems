class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def bsearch(left, right):
     
            # if left==right and matrix[left//n][left//n] != target:
            #     return False

            if left > right :
                return False
            
            mid = (left+right)//2
            if target==matrix[mid//n][mid%n]:
                return True
            elif target < matrix[mid//n][mid%n]:
                return bsearch(left, mid)
            elif target > matrix[mid//n][mid%n] : 
                return bsearch(mid+1, right)
        return bsearch(0, m*n-1)
        