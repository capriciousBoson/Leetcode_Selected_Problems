class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        sorted_events = sorted(events)
        n = len(events)
        # visited = [False for e in events]
        max_days = events[0][1]
        for s,e in events:
            max_days = max(max_days, e)

        res = 0
        heap = []
        idx = 0

        for day in range(max_days+1):
            while idx < n and sorted_events[idx][0] <= day:
                s,e = sorted_events[idx]
                heapq.heappush(heap, e)
                idx += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap : 
                e = heapq.heappop(heap)
                # visited[event] = True
                res += 1

        return res

        