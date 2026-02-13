import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, [-val, key])
        
        res = []
        for _ in range(k):
            n = heapq.heappop(heap)[1]
            res.append(n)   
        return res     
        