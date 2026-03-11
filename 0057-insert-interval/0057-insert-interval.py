class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: 
            return [newInterval]

        res = []
        inserted = False

        i = 0
        while i < n:
            # clean insert
            if (
                not inserted
                and newInterval[0] < intervals[i][0]
                and newInterval[1] < intervals[i][0] ):

                res.append(newInterval)
                res.append(intervals[i])
                inserted = True
                i += 1
                continue
            
            # insert and merge
            elif (
                not inserted
                and ( intervals[i][0] <= newInterval[0] <= intervals[i][1]
                or newInterval[0] <= intervals[i][0] <= newInterval[1])) : 

                start = min(newInterval[0], intervals[i][0])
                end = newInterval[1]
        
                while i < n and end >= intervals[i][0]:
                    end = max(end, intervals[i][1])
                    i += 1
                res.append([start, end])
                inserted = True
                continue
            else:
                res.append(intervals[i])
                i += 1

        if not inserted: res.append(newInterval)
        return res

