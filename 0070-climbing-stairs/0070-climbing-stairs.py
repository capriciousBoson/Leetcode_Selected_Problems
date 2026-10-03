class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        memo = {}

        def climb(x):
            if x==n:
                return 1
            if x > n:
                return 0
            
            if x not in memo:
                memo[x] = climb(x+1) + climb(x+2)
            
            return memo[x]
        
        return climb(0)
        