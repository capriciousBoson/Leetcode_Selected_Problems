class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n==0:
            return [newInterval]
        res = []

        i = 0
        inserted =  False
        while i<n:
            # print(f"\nintervals[{i}] : {intervals[i]}")
            if not inserted and newInterval[0] < intervals[i][0] and newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                inserted  = True
                continue
            if (
                not inserted
                and intervals[i][0] <=  newInterval[0] <= intervals[i][1]
                or newInterval[0] <= intervals[i][0] <= newInterval[1] ):

                start = min(intervals[i][0], newInterval[0])
                while i < n and newInterval[1] > intervals[i][1]:
                    i += 1
                if  i< n and newInterval[1] >= intervals[i][0]:
                    end = max(newInterval[1], intervals[i][1])
                    i += 1
                    
                else:
                    end = newInterval[1]

                res.append([start, end])
                inserted = True
                continue
            res.append(intervals[i])
            i += 1
        if not inserted:
            res.append(newInterval)
        return res
