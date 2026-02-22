class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i1, i2):
            if i1>=len(s1) and i2>= len(s2) and i1+i2 >= len(s3):
                return True
            if i1+i2 >= len(s3):
                return False
            
            if (i1,i2) not in memo:


                res = False
                if i1 < len(s1) and s1[i1]==s3[i1+i2]:
                    res = res or dfs(i1+1, i2)
                if i2 < len(s2) and s2[i2] == s3[i1+i2]:
                    res = res or dfs(i1, i2+1)      
                memo[(i1,i2)] = res  

            return memo[(i1,i2)]    
        return dfs(0,0)