from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[-val, key] for  key,val in c.items()]
        heapq.heapify(freq)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freq)[1])
        return res
