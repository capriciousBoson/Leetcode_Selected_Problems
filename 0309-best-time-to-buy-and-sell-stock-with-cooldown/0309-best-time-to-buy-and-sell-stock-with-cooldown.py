class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next_row = [0,0]
        next_row2 = [0,0]

        for i in range(len(prices)-1, -1, -1):
            current_row = [0,0]
            for state in range(2):
                if state == 0:
                    buy = -prices[i] + next_row[1]
                    not_buy = next_row[0]
                    current_row[state] =  max(buy, not_buy)
                if state == 1:
                    sell = prices[i] + next_row2[0]
                    not_sell = next_row[1]
                    current_row[state] = max(sell, not_sell)

            next_row2 = next_row
            next_row = current_row

        return next_row[0]

        
        
        # state 0 - not bought
        # state 1 - bought
        # memo = {}
        # def dfs(i, state):
        #     if i>= len(prices):
        #         return 0
            
        #     if (i, state) not in memo:
        #         if state == 0:
        #             buy = -prices[i] + dfs(i+1, 1)
        #             not_buy = dfs(i+1, 0)
        #             memo[(i, state)] =  max(buy, not_buy)
        #         if state == 1:
        #             sell = prices[i] + dfs(i+2, 0)
        #             not_sell = dfs(i+1, 1)
        #             memo[(i, state)] = max(sell, not_sell)

        #     return memo[(i, state)]       
        # return dfs(0,0)
        