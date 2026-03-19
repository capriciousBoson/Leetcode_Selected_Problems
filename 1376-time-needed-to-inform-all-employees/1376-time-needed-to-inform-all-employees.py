# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.children = []


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        emps = {}
        for e,m in enumerate(manager):
            if m not in emps:
                emps[m] = []
            emps[m].append(e)
        
        def dfs(m):
            if m not in emps:
                return 0
            
            t = 0
            for e in emps[m]:
                t = max(t, dfs(e))
            return informTime[m] + t
        return dfs(headID)
 
