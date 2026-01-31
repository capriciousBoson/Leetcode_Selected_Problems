class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True) #g = 6 5 3 2, 1
        s.sort(reverse=True) #s = 5 4 1
        res = 0                 # res =  2
        while g and s:
            if s[-1]>=g[-1]:
                res += 1
                g.pop()
                s.pop()
            else:
                s.pop()
        return res

# greed = [3,7,9] , cookie = [10,9,6]

        