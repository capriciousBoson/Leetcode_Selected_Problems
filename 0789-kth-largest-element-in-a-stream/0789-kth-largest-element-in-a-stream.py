class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        self.kth_largest = None

    def findKthLargest(self):
        if len(self.heap) < self.k:
            return

        for i in range(len(self.heap)-self.k):
            heapq.heappop(self.heap)
        self.kth_largest = self.heap[0]




    def add(self, val: int) -> int:
        if not self.kth_largest:
            heapq.heappush(self.heap, val)
            self.findKthLargest()

        elif val > self.kth_largest:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
            self.kth_largest = self.heap[0]
        return self.kth_largest

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)