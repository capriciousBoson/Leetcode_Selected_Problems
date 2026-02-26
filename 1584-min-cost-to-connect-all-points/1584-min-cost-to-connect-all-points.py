class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        def weight(i,j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])

        dist = {(x,y):float('inf') for [x,y] in points}
        h = []

        
        
        heapq.heappush(h, (0, 0,-1))
        visited = [False for _ in points]

        print(f"h : {h}")
        res = 0
        while h:
            d,node, parent = heapq.heappop(h)
            if visited[node]: continue
            visited[node] = True
            res += d
            for idx in range(n):
                if idx == node or idx==parent : continue
                d_ = weight(node, idx)
                heapq.heappush(h, (d_, idx, node))

        return res




        # print(F"dist : {dist}")            



 





















        # cost = [[float('inf') for _ in range(n)] for __ in range(n)]

        # for i in range(n):
        #     for j in range(n):
        #         dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        #         cost[i][j] = dist

        # res = 0
        # for k in range(n):
        #     for r in range(n):
        #         if k==r: continue
        #         for c in range(n):
        #             if c==k: continue
        #             cost[r][c] = min(cost[r][c], cost[r][k]+cost[k][r]) 
        #             res += cost[r][c]

        # for row in cost:
        #     print(row)

        # return res//2
                