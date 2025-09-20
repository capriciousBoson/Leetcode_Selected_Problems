class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)   # v → u (take v before u)
        
        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(node):
            if state[node] == 1:  # cycle found
                return False
            if state[node] == 2:  # already processed
                return True
            
            state[node] = 1  # mark as visiting
            for ngh in adj[node]:
                if not dfs(ngh):
                    return False
            state[node] = 2  # mark as fully visited
            return True
        
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        
        return True
