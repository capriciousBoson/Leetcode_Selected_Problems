class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[left]<=nums[mid]:
                res = min(res, nums[left])
                left = mid+1
            else:
                res = min(res, nums[mid])
                right = mid-1


        return res
