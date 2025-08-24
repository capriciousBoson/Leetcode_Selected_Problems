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
        if not node: return 
        node_map = {}

        Q = collections.deque()
        Q.append(node)

        while Q:
            current = Q.popleft()
            node_map[current] = Node(current.val)

            for ngh in current.neighbors:
                if  ngh not in node_map:
                    Q.append(ngh)
        # print(node_map)
        # return
        for  old_node, new_node in node_map.items():
            for ngh in old_node.neighbors:
                new_node.neighbors.append(node_map[ngh])
        return node_map[node]

        