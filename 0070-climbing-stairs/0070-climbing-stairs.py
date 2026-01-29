class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(x):
            if x==n:
                return 1
            elif x>n:
                return 0
            
            if x not in memo:
                memo[x] = dp(x+1) + dp(x+2)
            return memo[x]
        return dp(0)

        