class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0: return 1
        if not coins: return 0

        memo = {}

        def dfs(i,x):
            if x==0:
                return 1
            if x<0 or i>=len(coins):
                return 0
            
            if (i, x) not in memo:

                memo[(i,x)] = dfs(i, x-coins[i]) + dfs(i+1, x)

            return memo[(i,x)]

        return dfs(0,amount)

        