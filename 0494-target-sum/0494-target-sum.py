class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        memo = {}
        def dfs(i,x):
            if i>=n:
                # print(f"final path sum : {x}")
                if x==target:
                    return 1
                else:
                    return 0
            if (i,x) not in memo:
                left = dfs(i+1, x+nums[i])
                right = dfs(i+1, x-nums[i])
                memo[(i,x)] = left + right

            return memo[(i,x)]


        res = dfs(0,0)
        return res
        