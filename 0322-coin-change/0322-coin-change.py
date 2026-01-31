class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return 0
        if amount==0: return 0

        memo = {}

        def fun(x):
            if x== 0:
                return 0
            elif x < 0:
                return float('inf')
            
            if x not in memo :
                res = float('inf')

                for c in coins:
                    res = min(res, 1 + fun(x-c))
                memo[x] = res

            return memo[x]
        n = fun(amount)
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

        