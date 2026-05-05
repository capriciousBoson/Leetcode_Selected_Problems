"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return

        node_map = {}

        q = collections.deque()
        q.append(node)

        while q:
            curr = q.popleft()

            new_node = Node(curr.val)
            node_map[curr] = new_node
            for ngh in curr.neighbors:
                if  ngh not in node_map:
                    q.append(ngh)

        for x in node_map:
            new_node = node_map[x]
            for ngh in x.neighbors:
                new_node.neighbors.append(node_map[ngh])



        return node_map[node]