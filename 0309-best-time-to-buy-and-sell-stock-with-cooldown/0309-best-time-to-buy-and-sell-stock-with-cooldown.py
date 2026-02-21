class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        # state 0 - not bought
        # state 1 - bought
        def dfs(i, state):
            if i>= len(prices):
                return 0
            
            if (i, state) not in memo:
                if state == 0:
                    buy = -prices[i] + dfs(i+1, 1)
                    not_buy = dfs(i+1, 0)
                    memo[(i, state)] =  max(buy, not_buy)
                if state == 1:
                    sell = prices[i] + dfs(i+2, 0)
                    not_sell = dfs(i+1, 1)
                    memo[(i, state)] = max(sell, not_sell)
                    
            return memo[(i, state)]       



        return dfs(0,0)
        