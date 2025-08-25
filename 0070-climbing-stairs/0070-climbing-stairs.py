class Solution:
    
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def climb(s):
        #     if s==0:
        #         return 1
        #     elif s<0:
        #         return 0
        #     if s not in memo:
        #         one_step = climb(s-1)
        #         two_step = climb(s-2)
        #         memo[s] = one_step + two_step
            
        #     return memo[s]
        # return climb(n)
        if n<2: return 1
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


        