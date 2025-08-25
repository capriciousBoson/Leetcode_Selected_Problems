class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}


        def minClimbCost(i):
            if i>=len(cost):
                return 0
            if i not in memo:
                memo[i] = cost[i] + min(minClimbCost(i+1), minClimbCost(i+2))
            return memo[i]
        return min(minClimbCost(0), minClimbCost(1))