# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2 : return
        if not list1: return list2
        if not list2: return list1


        curr1, curr2 = list1, list2
        head = list1
        if list2.val < list1.val:
            head = list2
            curr2 = list2.next
        else:
            curr1 = list1.next
        curr = head

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            else:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next

        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2
        
        return head




        