class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def robber(i):
            if i>=n:
                return 0
            if i not in memo:
                memo[i] = max(nums[i]+robber(i+2), robber(i+1))
            return memo[i]
        return robber(0)
        