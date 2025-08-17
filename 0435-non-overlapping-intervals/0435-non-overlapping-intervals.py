from collections import defaultdict
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        last = intervals[0]
        count = 1
        for i in range(1,n):
            if intervals[i][0] >= last[1]:
                count += 1
                last = intervals[i]
        
        return n-count





        