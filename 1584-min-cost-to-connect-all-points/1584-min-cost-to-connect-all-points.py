class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False for _ in points]
        
        n = len(points)
        res = 0
        heap = [[0, 0]]
        edges = 0

        while heap and edges < n:
            wt,node = heapq.heappop(heap)

            if visited[node] : continue
            visited[node] = True

            res += wt
            edges += 1

            for ngh in range(n):
                if visited[ngh] : continue

                new_wt = abs(points[node][0]-points[ngh][0]) \
                        + abs(points[node][1]-points[ngh][1])

                heapq.heappush(heap, [new_wt,ngh])

        return res
        