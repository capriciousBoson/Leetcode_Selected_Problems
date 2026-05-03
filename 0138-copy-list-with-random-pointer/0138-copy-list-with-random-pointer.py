
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        node_map = {}
        curr = head

        while  curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        current = head

        while current:
            new_node = node_map[current]
            if current.next is not None:
                new_node.next = node_map[current.next]
            
            if current.random is not None:
                new_node.random = node_map[current.random]

            current = current.next

        return node_map[head]