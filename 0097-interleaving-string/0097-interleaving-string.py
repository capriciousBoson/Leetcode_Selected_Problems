class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i1, i2, i3):
            if i1>=len(s1) and i2>= len(s2) and i3 >= len(s3):
                return True
            if i3 >= len(s3):
                return False
            
            if (i1,i2,i3) not in memo:


                res = False
                if i1 < len(s1) and s1[i1]==s3[i3]:
                    res = res or dfs(i1+1, i2, i3+1)
                if i2 < len(s2) and s2[i2] == s3[i3]:
                    res = res or dfs(i1, i2+1, i3+1)      
                memo[(i1,i2,i3)] = res  

            return memo[(i1,i2,i3)]    
        return dfs(0,0,0)