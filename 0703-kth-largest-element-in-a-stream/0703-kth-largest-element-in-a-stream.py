class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k
        
    
    def _shrink_to_k(self):
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self._shrink_to_k()
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)