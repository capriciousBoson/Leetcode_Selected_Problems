class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDistance(point1, point2):
            return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

        n = len(points)
        # adj = collections.defaultdict(list)

        # for i in range(n):
        #     for j in range(n):
        #         if i==j: continue
        #         adj[i].append([manhattanDistance(points[i], points[j]),j])
        #         adj[j].append([manhattanDistance(points[j], points[i]),i])
        # for key, val in adj.items():
        #     print(key, val)
        
        visited = [False for _ in range(len(points))]
        mst = []
        res = 0
        heap = [[0, 0, -1]]
        edges_added = 0

        while heap and edges_added<len(points):
            wt, node, parent = heapq.heappop(heap)
            if visited[node]: continue

            visited[node] = True
            res += wt

            if parent != -1:
                # visited[parent] = True
                edges_added += 1
                mst.append([parent, node])

            for ngh in range(n):
                if not visited[ngh]:
                    ngh_wt = manhattanDistance(points[ngh], points[node])
                    heapq.heappush(heap, [ngh_wt, ngh, node])
        # print(f"mst : {mst}, res = {res}")
        return res
