class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        eid = {}
    

        adj = collections.defaultdict(list)

        for i,[u,v] in enumerate(edges):
            adj[u].append(v)
            adj[v].append(u)
            eid[(u,v)] = i
            eid[(v,u)] = i

        heap = []
        heapq.heappush(heap, [-1, start_node])
        visited = [False for i in range(n)]

        # res = -float('inf')

        while heap:
            p,node = heapq.heappop(heap)

            visited[node] = True

            if node == end_node:
                return -p

            for ngh in adj[node]:
                print(f"ngh - {ngh}")
                if not visited[ngh]:

                    heapq.heappush(heap, [p*succProb[eid[(ngh, node)]], ngh])

    
        return 0


        