class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)
        # print(f"nb :{nb}, na :{na}")

        t  = 2
        if na <= nb:
            t += nb//na
        ra = a
        
        l = 0
        while l < len(a):
            i = 0
            r = l
            count = 1
            while a[r] == b[i]:
                # print(f"count = {count} | a[{r}] = {a[r]} | b[{i}] = {b[i]}")
                r += 1
                i += 1
                if i == len(b):
                    return count
                if r == len(a):
                    r = 0
                    count += 1
            
            l += 1
            if count > t:
                break

        return -1
