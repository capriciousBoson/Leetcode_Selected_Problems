class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        n = len(queries)
        res = [-1 for x in range(n)]
        sorted_queries = sorted([[q, index] for index,q in enumerate(queries)])


        heap = []
        idx = 0
        for q,i in sorted_queries:
    
            print(f"\nq, i : {q, i}---")
            
            while idx< len(intervals) and q >= intervals[idx][0]:
                s, e = intervals[idx]
                heapq.heappush(heap, [e-s+1, e])
                idx += 1
            while heap  and heap[0][1] < q:
                heapq.heappop(heap)
            if heap: res[i] = heap[0][0]
        return res


                


        