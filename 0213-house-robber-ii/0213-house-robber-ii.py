class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        n = len(nums)
        if n==1:
            return nums[0]
        def _rob(i):
            # nonlocal n
            
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + _rob(i+2), _rob(i+1))
            
            return memo[i]

        rob_nth = _rob(1)
        n -= 1
        memo = {}
        rob_1st =  _rob(0)

        return max(rob_nth, rob_1st)