class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {}
        for u,v,w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append([v,w])

        min_time = [float('inf') for _ in range(n+1)]
        min_time[k] = 0
        q = collections.deque([[k, 0]])

        while q:
            node,t = q.popleft()

            if node not in adj:
                continue
            for ngh,nt in adj[node]:
                if t+nt < min_time[ngh]:
                    min_time[ngh] = t+nt
                    q.append([ngh, min_time[ngh]])
        
        max_time = max(min_time[1:])
        print(f"max_time : {max_time} | \nmin_times : {min_time}")
        if max_time == float('inf'):
            return -1
        return max_time

        