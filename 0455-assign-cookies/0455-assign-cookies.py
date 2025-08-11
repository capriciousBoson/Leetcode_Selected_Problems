class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)
        res = 0

        while g and s:
            if s[0]>=g[0]:
                res += 1
                heapq.heappop(s)
                heapq.heappop(g)
            else:
                heapq.heappop(s)
        return res

        