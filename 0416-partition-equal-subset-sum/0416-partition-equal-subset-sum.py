class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums)%2 != 0: return False
        n = len(nums)

        dp = [[False for _ in range(target+1)] for __ in range(n+1)]

        for row in dp:
            row[0] = True
            # for number in nums:
            #     if number <=target:
            #         row[number] = True

        for i in range(1,n):
            for x in range(1, target+1):

                take = False

                if x-nums[i] >= 0 :
                    take = dp[i-1][x-nums[i]]
                not_take = dp[i-1][x]

                dp[i][x] = take or not_take

        # for row in dp:
        #     print(row)
        return dp[n-1][target]





        

        # memo = {}
        # def fun(i,x):
        #     if x==0:
        #         return True
        #     if x< 0 or i>=n:
        #         return False

            
        #     if (i,x) not in memo:
        #         take = fun(i+1, x-nums[i])
        #         if take: 
        #             return True
        #         not_take = fun(i+1, x)
        #         if not_take:
        #             return True
        #         memo[(i,x)] = take or not_take
        #     return memo[(i,x)]

        # return fun(0,target)

