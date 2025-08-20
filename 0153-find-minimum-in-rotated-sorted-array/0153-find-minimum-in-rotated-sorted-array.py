class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        # for n in nums:
        #     res = min(res, n)
        # return res
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if nums[left]<=nums[mid]:            # check if left half is sorted
                res = min(res, nums[left])
                left = mid+1
            else:                                # right half is sorted
                res = min(res, nums[mid])
                right = mid-1
        return res
