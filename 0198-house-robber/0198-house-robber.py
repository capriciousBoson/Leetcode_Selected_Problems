class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = {}
        # def robber(i):
        #     if i>=n:
        #         return 0
        #     if i not in memo:
        #         memo[i] = max(nums[i]+robber(i+2), robber(i+1))
        #     return memo[i]
        # return robber(0)
        
        dp = [0 for _  in range(n+1)]
        dp[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]