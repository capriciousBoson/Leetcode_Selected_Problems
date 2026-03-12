class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        n = len(flowers)
        people_s = sorted([[p,i] for i,p in enumerate(people)])
        flowers.sort(key=lambda x : x[0])

        res = [0 for _ in people_s]

        idx = 0
        minHeap = []
        for p, i in people_s:
            while idx < n and p >= flowers[idx][0] :
                heapq.heappush(minHeap, flowers[idx][1])
                idx += 1
            
            while minHeap and minHeap[0] < p:
                heapq.heappop(minHeap)
            res[i] = len(minHeap)

        return res


        