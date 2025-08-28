class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]

        res = nums[0]
        current_max = 0
        for i in range( len(nums)):
            current_max += nums[i]
            res = max(res, current_max)
            if current_max <=0:
                current_max = 0
        return res

            

        