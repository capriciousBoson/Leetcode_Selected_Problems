class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}


        # def minClimbCost(i):
        #     if i>=len(cost):
        #         return 0
        #     if i not in memo:
        #         memo[i] = cost[i] + min(minClimbCost(i+1), minClimbCost(i+2))
        #     return memo[i]
        # return min(minClimbCost(0), minClimbCost(1))
        n = len(cost)
        dp = [0 for _ in range(len(cost) + 1)]
        dp[n-1] = cost[n-1]
        dp[n] = 0

        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])
