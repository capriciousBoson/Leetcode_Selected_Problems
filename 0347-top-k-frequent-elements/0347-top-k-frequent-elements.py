class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        max_heap = []
        for n, f in freq.items():
            heapq.heappush(max_heap, [-f, n])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res
        