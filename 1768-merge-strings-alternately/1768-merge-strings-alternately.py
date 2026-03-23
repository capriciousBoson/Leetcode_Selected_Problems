class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1, i2 = 0,0
        res = ""

        while i1 < len(word1) and i2<len(word2):
            if i1==i2:
                res += word1[i1]
                i1 += 1
            else:
                res += word2[i2]
                i2 += 1
        
        if i1<len(word1):
            res += word1[i1:]
        elif i2<len(word2):
            res += word2[i2:]

        return res
