class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(i):
            if i>=n:
                return 0
            
            if i not in memo:
                rob = nums[i] + dp(i+2)
                dont_rob = dp(i+1)
                memo[i] = max(rob, dont_rob)
            return memo[i]
        return dp(0)

        