class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone_weight in stones:
            heapq.heappush(max_heap, -1*stone_weight)
        
        while len(max_heap) > 1:
            y = -1*heapq.heappop(max_heap)
            x = -1*heapq.heappop(max_heap)

            if y>x:
                heapq.heappush(max_heap, -1*(y-x))
        
        if len(max_heap)==1:
            return -1*max_heap[0]
        return 0
        