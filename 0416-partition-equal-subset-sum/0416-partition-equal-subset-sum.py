class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 !=0 or len(nums) < 2:
            return False
        
        n = len(nums)

        memo = {}

        def partitionSum(i,x):
            if x==total//2:
                return True
            if i>=n:
                return False
            
            if (i,x) not in memo:
                memo[(i,x)] = partitionSum(i+1, x) or partitionSum(i+1, x+nums[i])
            
            return memo[(i,x)]

        return partitionSum(0,0)
            

        # dp = [[False for _ in range((total//2) + 1)] for __ in range(n)]
        # if nums[0] <=total//2:
        #     dp[0][nums[0]] = True
        # for i in range(n):
        #     dp[i][0] = True
        
        # for i in range(1,n):
        #     for target in range(1,(total//2)+1):
        #         take = False
        #         if nums[i] <= target:
        #             take = dp[i-1][target-nums[i]]
        #         not_take = dp[i-1][target]
        #         dp[i][target] = take or not_take
        # return dp[n-1][total//2]

        


        # memo = {}
        # def fun(i,target):
        #     if target==0:
        #         return True
        #     if i==0:
        #         return target==nums[0]

        #     if (i, target) not in memo:
        #         take = False
        #         if target >= nums[i]:
        #             take =  fun(i-1, target - nums[i])
        #         if take==True: return True
        #         not_take = fun(i-1, target)
        #         if not_take==True: return True

        #         memo[(i,target)] = take or not_take
        #     return memo[(i, target)]
        # return fun(len(nums)-1, total//2)