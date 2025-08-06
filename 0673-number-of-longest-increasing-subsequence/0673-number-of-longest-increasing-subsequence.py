from collections import Counter
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        counts = [1 for _  in range(n)]
        res = 1
       

        for i in range(n):
            for prev in range(i):
                if nums[i]>nums[prev]:
                    # dp[i] = max(dp[i], 1+dp[prev])
                    if dp[i] < 1 + dp[prev]:
                        dp[i] = 1 + dp[prev]
                        counts[i] = counts[prev]
                    elif dp[i] == 1 + dp[prev]:
                        counts[i] += counts[prev]
    
            if dp[i]>res:
                res = dp[i]


        print(f"dp : {dp}")
        ans = 0
        for i in range(n):
            if dp[i]==res:
                ans += counts[i]

        return ans
        