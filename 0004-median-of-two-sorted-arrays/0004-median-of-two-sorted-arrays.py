class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = []
        for n1 in nums1:
            heapq.heappush(heap, n1)
        for n2 in nums2:
            heapq.heappush(heap, n2)
        n = len(heap)
        if n==1: return heap[0]
        left_median = 0
        right_median = 0
        # print(f"heap : {heap}")
        for _ in range((n//2)-1):
            heapq.heappop(heap)
        # print(f"after popping heap : {heap}")
        left_median = heapq.heappop(heap)
        right_median = heapq.heappop(heap)
        # print(f"left : {left_median} right : {right_median}")
        if n%2:
            return right_median
        return (left_median+right_median)/2

        