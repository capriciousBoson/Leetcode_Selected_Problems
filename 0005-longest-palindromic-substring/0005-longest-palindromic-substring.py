class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        max_lps = ""

        for i in range(n):
            for l, r in [(i,i), (i,i+1)]:
                while l>=0 and r <n and s[l]==s[r]:
                    
                    size = r-l+1
                    if size >max_len:
                        max_len = size
                        max_lps = s[l:r+1]
                    l -= 1
                    r += 1


        return max_lps
        