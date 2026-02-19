class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_str = ""

        def helper(l, r):
            nonlocal max_length, max_str
            if l>r:
                return
            if l<0 or r >= len(s):
                return

            if s[l]==s[r]:
                length = r-l  +1
                if length > max_length :
                    max_length = length
                    max_str = s[l:r+1]
                helper(l-1, r+1)

        for i in range(len(s)):
            helper(i,i)

            helper(i,i+1)

        return max_str
                

        
                
        