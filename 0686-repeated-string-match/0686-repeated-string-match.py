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
            # print(f"checking for sbustring in ra : {ra}, x :{x}")
            for i in range(0, na*(x)-nb+1):
                # print(f"starting at ra[{i}] = {ra[i]} ")
                if b[0]==ra[i]:
                    m = i + nb
                    # print(f"nb :{nb}, i : {i}, m : {m}")
                    
                    # print(f"b : {b} and substr  : {ra[i:m]}")
                    if b == ra[i:m]:
                        return x
        return -1 