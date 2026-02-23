class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegrees = [0 for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[v].append(u)
            indegrees[u] += 1
        q = collections.deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        # print(f"adj : {adj} \nindegrees : {indegrees} \nq : {q}")


        toposort = []
        while q:
            node = q.popleft()
            toposort.append(node)

            for ngh in adj[node]:
                indegrees[ngh] -= 1
                # print(f" indegrees : {indegrees}")
                if indegrees[ngh] == 0:
                    q.append(ngh)

        # print(f"toposort : {toposort}")
        return toposort if len(toposort)==numCourses else []