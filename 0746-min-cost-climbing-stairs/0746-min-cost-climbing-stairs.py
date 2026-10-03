class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost = float('inf')
        memo = {}
        
        def climb(i):
            nonlocal min_cost

            if i >= len(cost):
                return 0

            if i not in memo:
                memo[i] = min(cost[i]+climb(i+1), cost[i]+climb(i+2))
            
            return memo[i]
        
        return min(climb(0), climb(1))




