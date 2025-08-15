class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        # n = len(intervals)
        heap = []
        n = 0
        for interval in intervals:
            n+=1
            heapq.heappush(heap, interval)

        res = [heapq.heappop(heap)]
        i = 1
        while i < n:
            current = heapq.heappop(heap)
            if current[0] <= res[-1][1]:
                end = max(current[1], res[-1][1])
                res[-1][1] = end
                i += 1
            else:
                res.append(current)
                i += 1
        return res
                
                
