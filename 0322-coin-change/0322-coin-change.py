class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range( amount+1):
            for coin in coins:
                if i+coin <= amount:
                    # print(f"for amount(i) : {i}, coin : {coin} dp[i+coin] : {dp[i+coin]}")
                    dp[i+coin] = min(dp[i+coin], 1+dp[i])
                    # print(f"updated  dp[i+coin] : {dp[i+coin]}")

        # print(f"final dp array : {dp}")
        return dp[amount] if dp[amount] != float('inf') else -1

        # memo = {}

        # def dfs( money):
        
        #     if money == amount:
        #         return 0
        #     if money > amount:
        #         return float('inf')

        #     if money in memo: 
        #         return memo[money]
        #     res = float('inf')
        #     for coin in coins:
        #         res =min(res, 1+ dfs(money+coin))

        #     memo[money] =res

        #     return  memo[money]
        
        # n = dfs(0)
        # if n==float('inf'): return -1
        # return n

            
        