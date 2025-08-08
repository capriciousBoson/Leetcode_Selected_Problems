import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*x for x in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            r=heapq.heappop(nums)
            print(r)
        return -1*heapq.heappop(nums)

        