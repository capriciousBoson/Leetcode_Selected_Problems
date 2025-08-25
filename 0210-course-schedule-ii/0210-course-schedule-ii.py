class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegrees = [0 for _ in range(numCourses)]

        for u,v in prerequisites:
            indegrees[v] += 1
            adj[u].append(v)

        res = []
        Q = collections.deque()
        for i in range(numCourses):
            if indegrees[i]==0:
                Q.append(i)
        
        while Q:
            node = Q.popleft()
            res.append(node)

            for ngh in adj[node]:

                indegrees[ngh] -= 1
                if indegrees[ngh] == 0:
                    Q.append(ngh)
        
        return res[::-1] if len(res)==numCourses else []
        