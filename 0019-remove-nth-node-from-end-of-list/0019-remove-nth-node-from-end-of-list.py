# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return
        if not head.next and n==1:
            return


        front = head
        back = head

        for _ in range(n):
            front = front.next

        if front is None:
            return head.next

        while front.next is not None:
            front = front.next
            back = back.next

        back.next = back.next.next
        return head 