class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not(-sum(nums)<=target<=sum(nums)):
            return 0

        n = len(nums)
        memo = {}

        def dp(i, x):
            if x==0 and i>=n:
                return 1
            if i >= n:
                return 0

            if (i,x) not in memo:
                memo[(i,x)] = dp(i+1, x-nums[i]) + dp(i+1, x+nums[i])
            return memo[(i,x)]

        return dp(0,target)
