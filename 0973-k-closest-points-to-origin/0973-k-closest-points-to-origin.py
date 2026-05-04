class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        for x,y in points:
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (d, x,y))
        
        res = []
        for _ in range(k):
            _, x,y = heapq.heappop(min_heap)
            res.append([x,y])

        return res 
        