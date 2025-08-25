class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegrees = [0 for _ in range(numCourses)]
        res = []
        Q = collections.deque()

        for u,v in prerequisites:
            indegrees[v] += 1
            adj[u].append(v)
        
        for i in range(numCourses):
            if indegrees[i]==0:
                Q.append(i)

        while Q:
            node = Q.popleft()
            res.append(node)
            for ngh in adj[node]:
                indegrees[ngh] -= 1
                if indegrees[ngh]==0:
                    Q.append(ngh)
        return len(res)==numCourses

        