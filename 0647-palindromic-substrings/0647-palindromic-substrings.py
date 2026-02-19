class Solution:
    def countSubstrings(self, s: str) -> int:


        def expand(l,r):
            # nonlocal ans
            if l> r or l<0 or r>=len(s):
                return 0
            if s[l]==s[r]:
                return 1 + expand(l-1, r+1)
            else:
                return 0
                
        a = 0
        for  i in range(len(s)):
            a += expand(i,i)
            a += expand(i, i+1)

        return a

        