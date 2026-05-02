# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr_head = head
        while curr and curr.next:
            ngh = curr.next
            curr.next = ngh.next
            ngh.next = curr_head
            curr_head = ngh
        
        return curr_head


        