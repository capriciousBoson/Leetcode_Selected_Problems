class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: 
            return [newInterval]

        idx  = bisect.bisect_left(intervals, newInterval)

        merge_idx = -1


        if idx-1 >= 0 and intervals[idx-1][0] <= newInterval[0] <= intervals[idx-1][1]:
            # print(f"adding to left")
            intervals[idx-1][1] = max(intervals[idx-1][1], newInterval[1])
            merge_idx = idx-1

        elif idx < n and  newInterval[1] >= intervals[idx][0] >= newInterval[0] : 
            # print(f"adding to right")
            intervals[idx][0] = newInterval[0]
            intervals[idx][1] = max(intervals[idx][1], newInterval[1])

            merge_idx = idx
        
        else:
            bisect.insort(intervals, newInterval)
    
        if merge_idx != -1:
            i = merge_idx
            while i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
                

        return intervals

        
