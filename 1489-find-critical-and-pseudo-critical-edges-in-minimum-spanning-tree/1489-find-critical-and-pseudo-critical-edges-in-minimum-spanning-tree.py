class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self, a,b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1


class Solution:
    def mst(self, edges, force, block, n):
        uf = UnionFind(n)

        weight = 0
        if force != -1:
            uf.union(edges[force][0], edges[force][1])
            weight += edges[force][2]
        
        for i in range(len(edges)):
            if i == block or i==force:
                continue

            u,v, w, _ = edges[i]
            if uf.find(u) != uf.find(v):
                uf.union(u,v)
                weight += w

        # print(f"uf.parent :{uf.parent}")
        for node in range(n):
        
            if uf.find(node) != uf.find(0):
                return float('inf')
        return weight


    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for i in range(len(edges)):
            edges[i].append(i)
        
        edges.sort(key=lambda x: x[2])
        
        base_mst_wt = self.mst(edges=edges, force=-1, block=-1, n=n)

        critical = []
        psuedo_critical = []

        for i in range(len(edges)):
            # block edge:
            blocked_wt = self.mst(edges=edges, force=-1, block=i, n=n)

            if blocked_wt > base_mst_wt:
                critical.append(edges[i][3])
                continue

            # force edge:
            forced_wt = self.mst(edges=edges, force=i, block=-1, n=n)

            if forced_wt == base_mst_wt:
                psuedo_critical.append(edges[i][3])

        return [critical, psuedo_critical]

