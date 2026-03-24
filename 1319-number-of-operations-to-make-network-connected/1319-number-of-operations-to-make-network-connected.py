class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        num_edges = len(connections)

        if num_edges < n-1 : 
            return -1

        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        def findParent(x):
            if parent[x] != x:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(u,v):

            root_u = findParent(u)
            root_v = findParent(v)

            if root_u == root_v:
                return
            
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                rank[root_v] += 1

        for u,v in connections:
            union(u,v)   

        components = set()
        for i in range(n):
            components.add(findParent(i))    
        return len(components) - 1   


        
