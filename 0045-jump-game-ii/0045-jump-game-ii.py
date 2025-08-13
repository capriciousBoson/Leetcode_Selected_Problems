class Solution:
    # def find_jump(self,ranges, i):
    #     for a,b,jumps in ranges:
    #         if a<=i<=b : return jumps

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return 0
        
        # dp = [[float('inf') for _  in range(n+1)] for __ in range(n+1)]
        # dp[0][0] = 0 

        # for i in range(n):
        #     min_jums = float('inf')
        #     for j in range(1, nums[i]+1):
        #         min_jumps = min(min_jumps, dp[i+x][j+1])


        memo = {}
        def dfs(i):
            if i >=n-1:

                return 0
            
            if (i) not in memo:
                min_jumps = float('inf')
                for x in range(1,nums[i]+1):
                    min_jumps = min(min_jumps, 1+dfs(i+x))
                memo[i] = min_jumps
            return memo[i]

        return dfs(0)

        


        # jumps = 0
        # end = 0        # end of the current jump's range
        # farthest = 0   # farthest we can reach while scanning this range

        # # We stop at n-2 because once we reach the last index, no more jumps are needed
        # for i in range(n - 1):
        #     farthest = max(farthest, i + nums[i])
        #     if i == end:
        #         jumps += 1
        #         end = farthest
        #         if end >= n - 1:
        #             break
        # return jumps




