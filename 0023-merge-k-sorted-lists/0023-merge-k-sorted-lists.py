# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp
        while True:

            min_head = float('inf')
            for l in lists:
                if not l:
                    continue
                if l.val < min_head:
                    min_head = l.val
            
            if min_head == float('inf'):
                break
            for i in range(len(lists)):
                node = lists[i]
                if node !=None and node.val==min_head:
                    lists[i] = node.next
                    node.next = None
                    curr.next = node
                    curr = curr.next

        return temp.next
     

