from collections import Counter
class Solution:
    def checkValidString(self, s: str) -> bool:
        minv, maxv = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                minv += 1
                maxv += 1
            elif s[i] == ')':
                minv -= 1
                maxv -= 1
            else:
                minv -=1
                maxv += 1
            if minv <0 :
                minv = 0
            if maxv < 0:
                return False

        print(f"range : {minv, maxv}")
        if minv >0 or maxv<0:
            return False
        return True
           