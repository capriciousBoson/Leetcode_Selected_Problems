import heapq

class Solution:
    def smallestRange(self, nums):
        k = len(nums)
        heap = []
        current_max = float('-inf')
        
        for i in range(k):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))
            current_max = max(current_max, val)
        
        best_range = [-10**5, 10**5]
        
        while True:
            min_val, row, col = heapq.heappop(heap)
            
            if current_max - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, current_max]
            
            if col + 1 == len(nums[row]):
                break
            
            next_val = nums[row][col + 1]
            heapq.heappush(heap, (next_val, row, col + 1))
            current_max = max(current_max, next_val)
        
        return best_range
        