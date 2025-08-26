class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        total = sum(nums)

        if not (-total <= target <= total):
            return 0

        memo = {}

        def dfs(i,x):
            if i>=len(nums):
                if x==target:
                    return 1
                else:
                    return 0
            
            if (i,x) not in memo:
                a = dfs(i+1, x + nums[i])
                b = dfs(i+1, x - nums[i])

                memo[(i,x)] = a+b
            return memo[(i,x)]

        return dfs(0, 0)
        