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
        
        # dp = [0 for _  in range(n+1)]
        dp_i1 = nums[n-1]
        dp_i2 = 0

        for i in range(n-2, -1, -1):
            x = max(nums[i] + dp_i2, dp_i1)
            dp_i2 = dp_i1
            dp_i1 = x
        return max(dp_i1, dp_i2)