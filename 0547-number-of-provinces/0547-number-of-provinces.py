class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]

        res = 0

        
        for i in range(n):
            # print(f"visited : {visited}")
            if not visited[i]:
                res += 1

                Q = collections.deque()
                Q.append(i)
                visited[i] = True
                while Q:
                    node = Q.popleft()
                    for ngh in range(n):
                        if isConnected[node][ngh]==1 and not visited[ngh]:
                            Q.append(ngh)
                            visited[ngh] = True
        return res
                
        