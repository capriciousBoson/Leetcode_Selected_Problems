class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}

        def expand(l,r):
            # nonlocal ans
            if l> r or l<0 or r>=len(s):
                return 0
            if (l,r) not in memo:
                if s[l]==s[r]:
                    memo[(l,r)] = 1 + expand(l-1, r+1)
                else:
                    memo[(l,r)] = 0
            return memo[(l,r)]
                
        a = 0
        for  i in range(len(s)):
            a += expand(i,i)
            a += expand(i, i+1)

        return a

        