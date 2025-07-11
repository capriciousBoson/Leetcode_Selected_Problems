class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total = sum(nums)

        if target > total or target < -total: 
            # print(f"total : {total}, target : {target}")
            return 0


        dp = [{} for _ in range(n)]

        dp[0][-nums[0]] = 1
        dp[0][nums[0]] = 1
        if nums[0]==0:
            dp[0][0] = 2

        for i in range(1, n):
            for val in dp[i-1]:
                plus_val = val + nums[i]
                minus_val = val - nums[i]

                if plus_val in dp[i]:
                    dp[i][plus_val] += dp[i-1][val]
                else:
                     dp[i][plus_val] =  dp[i-1][val]

                if minus_val in dp[i]:
                    dp[i][minus_val] += dp[i-1][val]
                else:
                    dp[i][minus_val] = dp[i-1][val]
        
        print(dp)

        return dp[n-1][target] if target in dp[n-1] else 0

            

        # memo = {}
        # def dfs(i,x):
        #     if i>=n:
        #         # print(f"final path sum : {x}")
        #         if x==target:
        #             return 1
        #         else:
        #             return 0
        #     if (i,x) not in memo:
        #         left = dfs(i+1, x+nums[i])
        #         right = dfs(i+1, x-nums[i])
        #         memo[(i,x)] = left + right

        #     return memo[(i,x)]


        # res = dfs(0,0)
        # return res
        