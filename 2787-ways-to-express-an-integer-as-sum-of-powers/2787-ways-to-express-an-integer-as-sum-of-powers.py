
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        max_num = math.ceil(math.pow(n, (1/x)))
        print(f"max num : {max_num}")

        dp = [[0 for _ in range(max_num+2)] for __ in range(n+2)]
        dp[n] = [1 for _ in range(max_num + 2)] 


        for val in range(n-1, -1, -1):
            for num in range(max_num, 0, -1):
                pick = 0
                if (val + math.ceil(math.pow(num, x))) <= n:
                    pick = dp[(val + math.ceil(math.pow(num, x)))][num+1]

                not_pick = dp[val][num+1]
                dp[val][num] = pick + not_pick

        return dp[0][1]%MOD
        
        # memo = {}
        # def dfs(val, num):
        #     # print(f"current val :    {val} | current num : {num}")
        #     if val == n:
        #         return 1

        #     if val > n :
        #         return 0
        #     if  num > max_num : 
        #         return 0
            

        #     if (val, num) not in memo :
        #         pick = dfs(val+ math.pow(num, x), num+1)
        #         not_pick = dfs(val, num+1)
        #         memo[(val, num)] = pick + not_pick

        #     return memo[(val, num)]

        # return dfs(0, 1)%MOD