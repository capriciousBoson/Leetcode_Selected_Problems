class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for k, l in enumerate(nums):
            heapq.heappush(heap, [l[0],0, k])

        right = max([l[0] for l in nums])
        min_range = float('inf')
        res = []

        while True:
            
            left, idx, k = heapq.heappop(heap)
            # print(f"\nleft,right :{left, right} , idx, k : { idx, k} ")


            curr_range = right - left
            if curr_range < min_range:
                min_range = curr_range
                res = [left, right]

            if idx == len(nums[k]) - 1:
                break
            else:
                heapq.heappush(heap, [nums[k][idx+1], idx+1, k])
                right = max(right, nums[k][idx+1])
            # print(f" heap  :{heap}")
        return res


