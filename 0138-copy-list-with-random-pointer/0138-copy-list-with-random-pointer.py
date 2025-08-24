"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None:None}
    

        current = head
        while current:
            node_map[current] = ListNode(current.val)
        
            current = current.next

        for oldnode, newnode in node_map.items():
            if oldnode is not None:
                newnode.next  = node_map.get(oldnode.next, None)
                newnode.random = node_map.get(oldnode.random, None)

        return node_map[head]
        
        