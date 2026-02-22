class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n1+n2 != n3:
            return False

        dp = [[False for _ in range(n2+1)] for __ in range(n1+1)]
        dp[n1][n2] = True
        # for i in range(n1+1):
        #     for j in range(n2+1):
        #         if i >= n1 and j>= n2 and i+j >= n3-1:
        #             dp[i][j] = True
        # dp[n1][n2-1] = True
        # dp[n1-1][n2] = True

        for row in dp:
            print(row)
        
        for i1 in range(n1,-1,-1):
            for i2 in range(n2, -1, -1):
                if i1==n1 and i2==n2: continue
                res = False
                if i1 < n1 and s1[i1] == s3[i1+i2]:
                    res = res or dp[i1+1][i2]
                if i2 < n2 and s2[i2] == s3[i1+i2]:
                    res = res or dp[i1][i2+1]
                dp[i1][i2] = res


        return dp[0][0]





        # memo = {}
        # def dfs(i1, i2):
        #     if i1>=len(s1) and i2>= len(s2) and i1+i2 >= len(s3):
        #         return True
        #     if i1+i2 >= len(s3):
        #         return False
            
        #     if (i1,i2) not in memo:


        #         res = False
        #         if i1 < len(s1) and s1[i1]==s3[i1+i2]:
        #             res = res or dfs(i1+1, i2)
        #         if i2 < len(s2) and s2[i2] == s3[i1+i2]:
        #             res = res or dfs(i1, i2+1)      
        #         memo[(i1,i2)] = res  

        #     return memo[(i1,i2)]    
        # return dfs(0,0)