class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        for eid, (u,v) in enumerate(tickets):
            heapq.heappush(adj[u], (v, eid))

        visited = [False for _ in tickets]

        res = []
        
        def dfs(u):
            while adj[u]:
                ngh, eid = heapq.heappop(adj[u])
                if visited[eid]:
                    continue
                visited[eid] = True
                dfs(ngh)
            
            res.append(u)
 
        dfs('JFK')
        print(res)
        return res[::-1]

        


            