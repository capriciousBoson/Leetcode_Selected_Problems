from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        found = {}
        l, r = 0,0

        while r < len(s):  
            if s[r] in found and found[s[r]] >= l:
                l = found[s[r]]+1

            found[s[r]] = r
            length = r-l +1
            res = max(length, res)
            r += 1
        return res




