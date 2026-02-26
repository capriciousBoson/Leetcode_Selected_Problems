class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        current = nums[0]
        for n in nums[1:]:
            
            if current <0:
                current = n
            else:
                current += n
            res = max(res, current)
        return res


        