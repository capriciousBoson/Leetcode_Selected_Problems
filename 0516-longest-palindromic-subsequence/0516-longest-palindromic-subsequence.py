class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if not n: return 0
        
        memo = {}
        rs = s[::-1]

        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if (i,j) not in memo:
                if s[i]==rs[j]:
                   memo[(i,j)] =  1 + dfs(i-1, j-1)
                else:
                    memo[(i,j)] = max(dfs(i-1, j), dfs(i, j-1))
            return memo[(i,j)]

        res = dfs(n-1,n-1)
        return res
        
        