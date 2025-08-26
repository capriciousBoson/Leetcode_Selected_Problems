class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return 0
        if amount==0: return 0
        memo = {}
        def dfs(x):
            if x==0:
                return 0
            if x<0 : return float('inf')

            if x not in memo:
                res = float('inf')
                for c in coins:
                    res = min(res, 1+dfs(x-c))
                memo[x] = res
            return memo[x]
        n = dfs(amount)
        return n if n!=float('inf') else -1

        