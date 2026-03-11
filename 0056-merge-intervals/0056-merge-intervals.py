class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        res = [intervals[0]]
        i = 1
        while i < n:
            # overlap
            if (res[-1][0] <= intervals[i][0] <= res[-1][1] 
                or intervals[i][0] <= res[-1][1] <= intervals[i][1] ):

                start = min(res[-1][0], intervals[i][0])
                end = max(intervals[i][1], res[-1][1])

                while  i < n and end >= intervals[i][0]:
                    end = max(end, intervals[i][1])
                    i += 1
                res[-1][0] = start
                res[-1][1] = end
                continue
            else:
                res.append(intervals[i])
                i += 1

        return res

        
        
