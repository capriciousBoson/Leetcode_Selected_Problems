class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for __ in range(len(text2)+1)]

        for i in range(len(text2)-1, -1, -1):
            for j in range(len(text1)-1, -1, -1):
                if text2[i]==text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
                

        
        # memo = {}
        # def dfs(i,j):
        #     if i >= len(text1) or j>= len(text2):
        #         return 0
        #     if (i,j) not in memo:
        #         if text1[i]==text2[j]:
        #             memo[(i,j)] = 1 + dfs(i+1, j+1)
        #         else:
        #             pick1 = dfs(i, j+1)
        #             pick2 = dfs(i+1, j)
        #             memo[(i,j)] = max(pick1, pick2)
        #     return memo[(i,j)]
        
        # return dfs(0,0)
        