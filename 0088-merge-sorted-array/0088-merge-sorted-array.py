class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i1, i2 = m-1,n-1

        if not n: return

        end = m+n - 1

        while i2 >=0 :
            
            if i1 < 0:
                nums1[end] = nums2[i2]
                i2 -= 1
                end -= 1
                continue


            if nums2[i2] >= nums1[i1]:
                nums1[end] = nums2[i2]
                i2 -= 1
                end -= 1

            else:
                nums1[end] = nums1[i1]
                nums1[i1] = 0
 
                i1 -= 1
                end -= 1





        