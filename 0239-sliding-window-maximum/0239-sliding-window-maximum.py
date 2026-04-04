class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        
        res = []
        max_heap = []
        
        for i in range(n):
            # expand the window
            heapq.heappush(max_heap, [-nums[i], i])

            if len(max_heap) <k:
                continue
            left = i - k +1
            while  max_heap[0][1] < left:
                heapq.heappop(max_heap)
            
            res.append(-max_heap[0][0])
        return res



        