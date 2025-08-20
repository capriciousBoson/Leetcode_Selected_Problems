class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def bsearch(l,r):
            if l==r and nums[l] != target:
                return -1



            mid = (l+r)//2

            if target==nums[mid]:
                return mid
            if target < nums[mid] : 
                return bsearch(l, mid)
            elif target > nums[mid]:
                return bsearch(mid+1, r)
        return bsearch(0,n-1)

        
        