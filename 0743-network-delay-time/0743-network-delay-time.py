class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_taken = [float('inf') for _ in range(n+1)]

        adj = collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append([v, w])
        # reach = 

        heap = []
        heapq.heappush(heap,[0,k])
        time_taken[k] = 0
        
        while heap:
            time, node = heapq.heappop(heap)
            
            for ngh, t in adj[node]:
                if time + t < time_taken[ngh]:
                    heapq.heappush(heap, [time + t, ngh])
                    time_taken[ngh] = time + t

        res = max(time_taken[1:])

        return res if res!=float('inf') else -1