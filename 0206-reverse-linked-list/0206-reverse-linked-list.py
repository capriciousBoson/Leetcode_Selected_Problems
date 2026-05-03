# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        stk = []
        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next
        
        new_head = stk.pop()
        curr = new_head
        while stk:
            curr.next = stk.pop()
            curr = curr.next
        curr.next = None
        return new_head



        