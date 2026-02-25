class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False for _ in range(n+1)]

        adj = collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append([v, w])
        # reach = 

        res = -float('inf')
        heap = []
        heapq.heappush(heap,[0,k])
        
        while heap:
            time, node = heapq.heappop(heap)
            # print(f"current node : {node} | time : {time}")
            
            

            if not visited[node]:
                visited[node] = True
                res = max(res, time)
                for ngh, t in adj[node]:
                    heapq.heappush(heap, [time + t, ngh])
        # print(f"adj : {adj}")
        # print(f"visited array : {visited}")
        return res if False not in visited[1:] else -1