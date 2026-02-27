class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        memo = {}
        def dfs(idx):
            if idx >= len(nums)-1:
                return 0
            if idx not in memo:
                res = float('inf')
                for x in range(1, nums[idx]+1):
                    res = min(res, 1+ dfs(idx + x))
                memo[(idx)] = res
            return memo[(idx)]
        return dfs(0)

        