class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            start_points = ((i,i), (i,i+1))

            for left, right in start_points:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
        return res
                
            