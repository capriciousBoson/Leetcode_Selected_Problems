# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # dummy = ListNode(0)
        # dummy.next = head
        back = head
        front = head

        if not head.next and n==1:
            return None
        
        # if not head.next.next :
        #     if n==1:
        #         head.next = None
        #         return head
        #     elif n==2:
        #         return head.next

        for _ in range(n):
            front = front.next
        if front is None: return head.next
        while front.next:
            front  = front.next
            back = back.next
        
        back.next = back.next.next
        return head
        