class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:


        adj = [[] for i in range(n)]

        for i,(u,v) in enumerate(edges):
            adj[u].append([v, succProb[i]])
            adj[v].append([u,succProb[i]])

        heap = [(-1, start_node)]
        max_probs = [0 for i in range(n)]
        max_probs[start_node] = 1

        while heap:
            p,node = heapq.heappop(heap)
            p *= -1

            if max_probs[node] > p:
                continue

            if node == end_node:
                return p

            max_probs[node] = p

            for ngh,sp in adj[node]:
                if p*sp > max_probs[ngh]:
                    heapq.heappush(heap, (-p*sp, ngh))

    
        return max_probs[end_node]


        