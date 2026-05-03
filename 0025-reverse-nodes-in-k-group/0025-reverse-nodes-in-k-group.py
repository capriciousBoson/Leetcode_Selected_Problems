# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = head
        prev_tail = dummy
        stk = []

        while current:
            print(f"processed : {current.val} | stk length = {len(stk)+1}")
            stk.append(current)
            current = current.next

            if len(stk) == k:
                left = stk.pop()
                current2 = left
                while stk:
                    current2.next = stk.pop()
                    current2 = current2.next
                prev_tail.next = left
                prev_tail = current2
                current2.next = current
             

        return dummy.next

        