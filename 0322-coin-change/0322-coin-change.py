class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}
        def  dp(x):
            if x == amount:
                return 0
            if x > amount:
                return float('inf')
            if x not in memo : 
                res = float('inf')
                for c in coins:
                    n = 1 + dp(x+c)
                    res = min(n, res)
                memo[x] = res
            return memo[x]
        return dp(0) if dp(0) != float('inf') else -1

        