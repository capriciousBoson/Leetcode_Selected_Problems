class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def decodeways(i):
            if i >= len(s):
                return 1
            


            if s[i]=='0':
                return 0
            
            if i not in memo:
                memo[i]= decodeways(i+1)

                n2 = int(s[i:i+2])
                if 10 <= n2 <=26  :
                    memo[i]+= decodeways(i+2)
                
            return memo[i]
        return decodeways(0)