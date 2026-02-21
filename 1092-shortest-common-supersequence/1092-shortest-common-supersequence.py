class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for _ in range(len(str2)  + 1)] for __ in range(len(str1)+1)]

        for i in range(len(str1)-1, -1, -1):
            for j in  range(len(str2)-1, -1, -1):
                if str1[i]==str2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        print(f" LCS : {dp[0][0]} \n")
        for row in dp:
            print(row)
        
        res = ""
        p,q = 0, 0

        while p < len(str1) and q < len(str2):
            if str1[p]==str2[q]:
                res = res + str1[p]
                p += 1
                q += 1
            else:
                if dp[p+1][q] >= dp[p][q+1]:
                    res = res + str1[p]
                    p = p+1
                else:
                    res = res + str2[q]
                    q = q+1

        # print(f" LCS string : {res}")
        while p < len(str1):
            res = res + str1[p]
            p += 1
        while q < len(str2):
            res = res + str2[q]
            q += 1

        print(f" supersequence : {res}")
        return res
                
