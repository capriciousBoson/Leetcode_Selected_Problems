class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return 0
        if amount==0: return 0
        
        # dp = [float('inf') for _ in range(amount + 1)]
        # dp[0] = 0
        # for c in coins:
        #     if c<= amount:
        #         dp[c] = 1

        # for x in range(amount+1):
        #     for c in coins:
                
        #         if x+c <= amount:
        #             dp[x] = min(dp[x], 1+ dp[x+c])
        # return dp[amount]



        memo = {}

        def fun(x):
            if x== amount:
                return 0
            elif x > amount:
                return float('inf')
            
            if x not in memo :
                res = float('inf')

                for c in coins:
                    res = min(res, 1 + fun(x+c))
                memo[x] = res

            return memo[x]
        n = fun(0)
        return n if n!=float('inf') else -1


        # n = len(coins)
        # dp = [float('inf') for _ in range(amount+1)]
        # dp[0] = 0

        # for a in range(1, amount+1):
        #     for coin in coins:
        #         if a-coin >=0:
        #             dp[a] = min(dp[a], 1+dp[a-coin])
                    
        # return dp[amount] if dp[amount]!=float('inf') else -1

        # memo = {}
        # def dfs(x):
        #     if x==0:
        #         return 0
        #     if x<0 : return float('inf')

        #     if x not in memo:
        #         res = float('inf')
        #         for c in coins:
        #             res = min(res, 1+dfs(x-c))
        #         memo[x] = res
        #     return memo[x]
        # n = dfs(amount)
        # return n if n!=float('inf') else -1

        