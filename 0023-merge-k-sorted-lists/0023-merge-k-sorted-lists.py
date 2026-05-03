# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp
        heap = []

        for i,ll in enumerate(lists):
            if ll is not None:

                heapq.heappush(heap,(ll.val, i))
        
        while heap:
            _, i = heapq.heappop(heap)
            node = lists[i]
            curr.next = node
            curr = curr.next
            if node.next:
                lists[i] = node.next
                heapq.heappush(heap, (node.next.val, i))





        return temp.next
     

