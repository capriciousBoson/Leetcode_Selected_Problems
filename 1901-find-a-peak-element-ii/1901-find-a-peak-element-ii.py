class Solution:
    # def check_peak(mat, i, j):
    def findPeakElement(self,arr):
        left = 0
        n = len(arr)
        right = n-1
        if n==1: return 0


        while left <= right:
            # print(arr[left:right+1])
            mid = (left + right)//2
            # print(arr[mid])

            if (mid==0 or arr[mid-1]<arr[mid]) and (mid==n-1 or arr[mid]>arr[mid+1]):
                return mid
            elif (mid==0 or arr[mid-1] < arr[mid]) :
                left = mid+1
                continue
            else:
                right = mid-1
                continue

    def maxElement(self, arr):
        max_n, max_i = 0, arr[0]
        for i, n in enumerate(arr):
            if n> max_n:
                max_n = n
                max_i = i
        return max_i

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        left, right = 0, m-1

        while left <= right:
            mid = (left + right)//2
            # print(f"mid : {mid}")
            # j = self.findPeakElement(mat[mid])
            j = self.maxElement(mat[mid])
            print(f"mid, j : {mat[mid], j}")


            print(f"current mid : mat[{mid,j}] =  {mat[mid][j]}")
            if ( 
                    (mid==0 or mat[mid-1][j] < mat[mid][j]) and 
                    (mid==m-1 or mat[mid+1][j] < mat[mid][j])
                ):
                return [mid,j]
            elif mid==0 or mat[mid-1][j]<mat[mid][j]:
                left = mid+1
            else:
                right = mid-1

        

 
