class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        x = 0
        res = float('inf')
        l = 0

        for i in range(len(nums)):
            x += nums[i]

            while  x >= target:
                res = min(res, i-l+1)
               
                x -= nums[l]
                l += 1

            

        return res if res!=float('inf') else 0
        