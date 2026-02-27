class Solution:
    def jump(self, nums: List[int]) -> int:
        reached = [float('inf') for _ in nums]
        reached[0]=0
        for i in range(len(nums)):
            for x in range(1, nums[i]+1):
                if i+x < len(nums):
                    reached[i+x] =   min(reached[i+x], 1+reached[i])
        return reached[-1]

        