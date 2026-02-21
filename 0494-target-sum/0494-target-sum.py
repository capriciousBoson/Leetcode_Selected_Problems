class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not(-sum(nums)<=target<=sum(nums)):
            return 0
        n = len(nums)

        offset = sum(nums)

        dp = [[0 for  _ in range(2*sum(nums)+1)] for  __ in range(n+1)]
        dp[n][0+offset] = 1

        for i in range(n-1, -1, -1):
            for x in range(2*sum(nums)+1):
                if x - nums[i] >= 0:
                    dp[i][x] += dp[i+1][x - nums[i]]
                if x + nums[i] <= 2*offset:
                    dp[i][x] += dp[i+1][x + nums[i]]
        # a = list(range(2*sum(nums)+1))
        # print(a)
        # for row in dp:
        #     print(row)
        
        return dp[0][target+offset]
                




  


        # memo = {}

        # def dp(i, x):
        #     if x==0 and i>=n:
        #         return 1
        #     if i >= n:
        #         return 0

        #     if (i,x) not in memo:
        #         memo[(i,x)] = dp(i+1, x-nums[i]) + dp(i+1, x+nums[i])
        #     return memo[(i,x)]

        # return dp(0,target)
