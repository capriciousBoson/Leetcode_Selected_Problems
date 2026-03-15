class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0 for c in s]

        left, right = 0, 1
        while right < len(s):
            if s[left] == s[right]:
                LPS[right] = left + 1
                left += 1
                right += 1
            else:
                if left > 0:
                    left = LPS[left - 1]
                else:
                    right += 1
        

  
        return  s[0:LPS[-1]]