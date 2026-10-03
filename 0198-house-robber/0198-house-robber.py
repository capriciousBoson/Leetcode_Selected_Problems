class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        
        def _rob(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + _rob(i+2), _rob(i+1))
            
            return memo[i]

        return _rob(0)
