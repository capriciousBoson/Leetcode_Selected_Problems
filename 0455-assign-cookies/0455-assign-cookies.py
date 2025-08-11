class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        while g and s:
            if s[-1]>=g[-1]:
                res += 1
                g.pop()
                s.pop()
            else:
                s.pop()
        return res

        