class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        stk = ['/']
        c = 0
        i = 0
        while i < len(num):
            while stk[-1] != '/' and int(stk[-1]) > int(num[i]) and c<k:

                stk.pop()
                c += 1
            stk.append(num[i])
            
            i += 1

        print(f"stk : {stk}, i : {i}")
        while c < k:
            stk.pop()
            c += 1
        res = ''
        for c in stk[1:]:
            res = res + c
        
        res = res + num[i:]
        while res and res[0] == '0':
            res = res[1:]
        return res if res else '0'



        


        