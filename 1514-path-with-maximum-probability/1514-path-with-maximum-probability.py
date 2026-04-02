class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:


        adj = collections.defaultdict(list)

        for i,[u,v] in enumerate(edges):
            adj[u].append([v, succProb[i]])
            adj[v].append([u,succProb[i]])

        heap = []
        heapq.heappush(heap, [-1, start_node])
        max_probs = [-float('inf') for i in range(n)]
        max_probs[start_node] = 1

        # res = -float('inf')

        while heap:
            p,node = heapq.heappop(heap)

            if max_probs[node] > -p:
                continue

            max_probs[node] = -p

            if node == end_node:
                return -p

            for ngh,sp in adj[node]:
                if -p*sp > max_probs[ngh]:
                    max_probs[ngh] = sp*p

                    heapq.heappush(heap, [p*sp, ngh])

    
        return 0


        