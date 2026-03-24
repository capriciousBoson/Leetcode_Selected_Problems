class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        adj = {}
        for u,v in connections:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False for _ in range(n)]
        mst_edges = 0

        q = collections.deque()

        for i in range(n):
            if not visited[i]:
                if i not in adj:
                    continue
                q.append([i, adj[i][0]])
                visited[i] = True

                while q:
                    parent, node = q.popleft()
                    visited[node] = True
                    mst_edges += 1
                    for ngh in adj[node]:
                        if not visited[ngh]:
                            q.append([node, ngh])

        return len(connections) - mst_edges

        
