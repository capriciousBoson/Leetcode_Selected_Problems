class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(s):
            if s==0:
                return 1
            elif s<0:
                return 0
            if s not in memo:
                one_step = climb(s-1)
                two_step = climb(s-2)
                memo[s] = one_step + two_step
            
            return memo[s]
        return climb(n)
        