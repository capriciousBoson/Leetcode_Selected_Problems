import bisect
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1]-x[0]+1)
        n = len(queries)
        res = [-1 for x in range(n)]
        queries = sorted([[q,i] for i,q in enumerate(queries)] )

        for left, right in intervals:
            q_idx = bisect.bisect_left(queries, [left])
            while q_idx < len(queries)  and queries[q_idx][0] <= right:
                i = queries.pop(q_idx)[1]
                res[i] = right-left+1
        return res



                


        