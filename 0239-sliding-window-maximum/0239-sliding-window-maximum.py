class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n= len(nums)

        res = []
        # prev_max = -float('inf')
        # prev_max_idx = -1

        left = 0
        right = k-1
        heap = []
        for i in range(k-1):
            heapq.heappush(heap, [-nums[i], i])


        while right < n:
            heapq.heappush(heap, [-nums[right], right])
            while heap[0][1] < left:
                heapq.heappop(heap)

            res.append(-heap[0][0])

            right += 1
            left += 1
            
        return res


        