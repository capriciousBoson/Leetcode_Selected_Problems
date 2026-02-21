class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i>= len(prices):
                return 0
            if i not in memo:

                profit = 0

                for idx in range(i+1, len(prices)):
                    profit = max(profit , prices[idx]-prices[i] + dfs(idx + 2), dfs(i+1))
                memo[i] = profit

            return memo[i]

        return dfs(0)
        