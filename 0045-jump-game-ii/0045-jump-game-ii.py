class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1 : return 0
        
        end, farthest, jumps = 0,0,0
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest
                if end >= n - 1:
                    return jumps




        # reached = [float('inf') for _ in nums]
        # reached[0]=0
        # for i in range(len(nums)):
        #     for x in range(1, nums[i]+1):
        #         if i+x < len(nums):
        #             reached[i+x] =   min(reached[i+x], 1+reached[i])
        # return reached[-1]

        