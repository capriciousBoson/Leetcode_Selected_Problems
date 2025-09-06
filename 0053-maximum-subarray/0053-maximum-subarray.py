class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]

        res = nums[0]
        current_max = 0
        # start = 0
        # end = 0
        for i in range( len(nums)):
            current_max += nums[i]
            # end = i
            res = max(res, current_max)
            if current_max <=0:
                current_max = 0
                # start = i+1
                # end = i+1
        # print(nums[start:end+1])
        return res

            

        