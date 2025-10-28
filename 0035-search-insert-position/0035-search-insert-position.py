class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def bsearch(l,r):
            print(l,r)

            if  r <0:
                return 0
            if l > n-1:
                return n

            if l>r :
                return l

            

            m = (l+r)//2
            if nums[m]==target:
                return m
            
            if l==r:
                if nums[l]>target:
                    return l
                else:
                    return l+1

            if target < nums[m] :
                return bsearch(l,m-1)
            elif target > nums[m]:
                return bsearch(m+1, r)
        return bsearch(0,n-1)
