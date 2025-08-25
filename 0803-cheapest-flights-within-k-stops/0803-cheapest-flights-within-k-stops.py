class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for frm, to, price in flights:
            adj[frm].append([to, price])
        
        distance = [float('inf') for _ in range(n)]
        stops_to = [float('inf') for _ in range(n)]

        heap = []
        heapq.heappush(heap, [0, 0,src])
        ans = float('inf')
        while heap:
            d, st, node = heapq.heappop(heap)
            if node==dst and st<=k+1:
                return d
            if st > k:
                continue
            
            for ngh, ngh_d in adj[node]:
                if ngh_d + d < distance[ngh] or st< stops_to[ngh]:
                    distance[ngh] = ngh_d + d
                    stops_to[ngh] = st
                    heapq.heappush(heap, [ngh_d + d, st+1,ngh])

        return -1
        