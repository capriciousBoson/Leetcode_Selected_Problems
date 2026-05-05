class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <2:
            return nums[0]

        dp = [0 for _ in range(n+1)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(
                dp[i-1],
                dp[i-2] + nums[i]
            )
        
        return dp[n-1]



        # memo = {}
        # def dp(i):
        #     if i>=n:
        #         return 0
            
        #     if i not in memo:
        #         rob = nums[i] + dp(i+2)
        #         dont_rob = dp(i+1)
        #         memo[i] = max(rob, dont_rob)
        #     return memo[i]
        # return dp(0)

        