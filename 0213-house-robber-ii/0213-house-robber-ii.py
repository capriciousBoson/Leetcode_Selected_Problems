class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n<2: return max(nums)
        
        def rob_(i):
            if i>=n:
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + rob_(i+2), rob_(i+1))
            return memo[i]

        x = rob_(1)
        n -=1 
        memo = {}
        y = rob_(0)
        return max(x,y)