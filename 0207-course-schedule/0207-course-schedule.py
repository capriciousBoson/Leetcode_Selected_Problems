class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        visited = [False for _ in range(numCourses)]
        path_visited = [False for _ in range(numCourses)]


        def dfs(node):
            visited[node] = True
            path_visited[node] = True
            for ngh in adj[node]:
                if not visited[ngh]:
                    if dfs(ngh):
                        return True
                elif visited[ngh] and path_visited[ngh]:
                    return True
            path_visited[node] = False
            return False

        for course in range(numCourses):
            if not visited[course]:
                cycle = dfs(course)
                if cycle:
                    return False
        return True