class Solution:
    def myAtoi(self, s: str) -> int:
        sign = None
        valid = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0,

        }

        def solve(s,num,sign):
            
            
            size = len(s)

            if not size: return num, sign
            if s[0] in valid:
                if not num:
                    num = 0
                num = num*10
                num += valid[s[0]]
                if not sign : sign = 1
            elif s[0] == "-":
                if not sign:
                    sign = -1
                else:
                    return num, sign
                
            elif s[0] == "+":
                if not sign:
                    sign = 1

                else:
                    return num, sign

            elif s[0] == " ":
                if sign:
                    return num, sign
                else: return solve(s[1:], num,sign)
            else: 
                return num, sign

            if size == 1:
                return num,sign
            else:
                return solve(s[1:], num,sign)
        num = None
        res,sign = solve(s, num,sign)
        if not res : res = 0
        if not sign : sign = 1
        res = res*sign
        if res < -2**31: return -2**31
        elif res > (2**31)-1 : return (2**31)-1
        else: return res
        