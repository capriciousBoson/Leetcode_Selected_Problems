"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return

        node_map = {}
        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            node_map[curr] = Node(curr.val)
            for ngh in curr.neighbors:
                if ngh not in node_map:
                    q.append(ngh)
        # print(f"node: map  :\n{node_map}")

        
        for old, new in node_map.items():
            for ngh in old.neighbors:
                new.neighbors.append(node_map[ngh])

        return node_map[node]



        