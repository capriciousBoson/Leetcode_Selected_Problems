from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        l,r = 0,0
        dq = defaultdict(int)
        dq[s[l]] = 1
        res = 1
        while r < len(s)-1:
            # print(f"\nstarting with string : {s[l:r+1]}  \tres : {res}")
            
            r += 1
            dq[s[r]] += 1
            # print(f"added one character : {s[l:r+1]}")
            
            # print(f"dq : {dq}")
            while dq[s[r]] > 1:
                dq[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            # print(f"final string : {s[l:r+1]} \t\t& res = {res}")
        return res







