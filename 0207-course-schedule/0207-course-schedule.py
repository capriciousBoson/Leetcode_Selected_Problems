from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for _ in range(numCourses)]
        path_visited = [False for _ in range(numCourses)]

        Adj = defaultdict(list)
        for a,b in prerequisites:
            Adj[b].append(a)
        
        def dfs(node):
            for ngh in Adj[node]:
                if not visited[ngh]:
                    visited[ngh] = True
                    path_visited[ngh] = True
                    if dfs(ngh) : return True
                elif visited[ngh] and path_visited[ngh]:
                    return True
            path_visited[node] = False
            return False

        for start in range(numCourses):
            if not visited[start]:
                visited[start] = True
                path_visited[start] = True
                if dfs(start):
                    return False
                path_visited[start] = False
                
        return True
        
        