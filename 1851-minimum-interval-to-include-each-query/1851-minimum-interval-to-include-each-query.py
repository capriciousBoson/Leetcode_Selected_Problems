class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        
        queries2 = [[i,q] for i,q in enumerate(queries)]
        queries2.sort(key = lambda x: x[0])

        intervals.sort(key = lambda x: x[0])

        res = [-1 for _ in queries]
        idx = 0

        for i,q in queries2:
            minHeap  = []

            while idx < len(intervals) and q >= intervals[idx][0]:
                s,e = intervals[idx]
                heapq.heappush(minHeap, [e-s+1,e])
                idx += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            if minHeap:
                res[i] = minHeap[0][0]

        return res
