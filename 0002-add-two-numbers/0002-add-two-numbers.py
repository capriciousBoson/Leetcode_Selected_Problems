# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2 : return
        if not l1:
            return l2
        elif not l2:
            return l1
        
        summation = l1.val + l2.val 
        carry = summation // 10
        ans = ListNode(summation%10)
        current = ans
        t1 = l1.next
        t2 = l2.next


        while t1 or t2 or carry:
            summation = carry
            if t1:
                summation += t1.val
                t1 = t1.next
            
            if t2:
                summation += t2.val
                t2 = t2.next

            current.next = ListNode(summation%10)

            carry = summation//10
            current = current.next

        return ans



