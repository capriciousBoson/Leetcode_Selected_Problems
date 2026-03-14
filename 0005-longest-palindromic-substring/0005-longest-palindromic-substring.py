class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_str = ""
        n = len(s)

        def dfs(l,r):
            nonlocal max_length, max_str
             
            if l <0 or r >= n:
                return 
            if s[l]!=s[r]:
                return

            if s[l]==s[r]:
                length = r-l + 1
                if  length > max_length:
                    max_length = length
                    max_str  = s[l:r+1]
                
                dfs(l-1, r+1)

        for i in range(n):
            dfs(i,i)
            dfs(i,i+1)
        return max_str