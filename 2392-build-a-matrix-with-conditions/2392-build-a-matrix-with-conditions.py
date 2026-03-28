class Solution:
    def topoSort(self,adj, indegrees):
        q = collections.deque()
        for node in indegrees:
            if indegrees[node] == 0:
                q.append(node)
        
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            
            if node in adj:
                for ngh in adj[node]:
                    indegrees[ngh] -= 1
                    if indegrees[ngh] == 0:
                        q.append(ngh)
        return order
    

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        matrix = [[0 for _ in range(k)] for __ in range(k)]

        row_indegrees = {i:0 for i in range(1,k+1)}
        row_adj = dict()

        for u,v in rowConditions:
            row_indegrees[v] += 1
            if u not in row_adj:
                row_adj[u] = []
            row_adj[u].append(v)

        col_adj = dict()
        col_indegrees = {i:0 for i in range(1,k+1)}

        for u, v in colConditions:
            col_indegrees[v] += 1
            if u not in col_adj:
                col_adj[u] = []
            col_adj[u].append(v)

        row_order = self.topoSort(row_adj, row_indegrees)
        if len(row_order) < k:
            return []
        
        col_order = self.topoSort(col_adj, col_indegrees)
        if len(col_order) < k:
            return []
        
        row_idx =dict()
        col_idx =dict()

        for i in range(k):
            row_idx[row_order[i]] = i
            col_idx[col_order[i]] = i
        
        for n in range(1,k+1):
            r,c = row_idx[n], col_idx[n]
            matrix[r][c] = n
        
        return matrix




        