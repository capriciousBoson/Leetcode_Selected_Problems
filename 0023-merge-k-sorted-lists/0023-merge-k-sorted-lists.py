# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not len(lists) :
            return 


        all_nodes = []
        counter = 0
        for head in lists:
            curr = head
            while curr:
                print(f"curr.val, curr = {curr.val, curr}")
                heapq.heappush(all_nodes, (curr.val,counter, curr))
                curr = curr.next
                counter +=1

        if not len(all_nodes): return
        # print(heapq.heappop(all_nodes)[2])
        res = heapq.heappop(all_nodes)[2]
        curr = res
        while all_nodes:
            curr.next = heapq.heappop(all_nodes)[2]
            curr = curr.next
        return res
                
        


        