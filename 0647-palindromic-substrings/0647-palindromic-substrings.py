class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def expand(l,r):
            nonlocal ans
            if l> r or l<0 or r>=len(s):
                return
            if s[l]==s[r]:
                ans += 1
                expand(l-1, r+1)
        
        for  i in range(len(s)):
            expand(i,i)
            expand(i, i+1)

        return ans

        