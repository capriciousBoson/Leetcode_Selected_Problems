class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)
        # print(f"nb :{nb}, na :{na}")

        t  = 2
        if na <= nb:
            t += nb//na

        for x in range( t+2):
            ra = a * x  
            for i in range(0, na*(x)-nb+1):
                
                if b in ra:
                    return x
        return -1 