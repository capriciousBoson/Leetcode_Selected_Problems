class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = collections.Counter(words)
        heap = []
        for word, freq in freqs.items():
            heapq.heappush(heap, [-freq, word])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res