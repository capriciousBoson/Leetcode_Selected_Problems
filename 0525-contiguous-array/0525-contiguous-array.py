class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffs = {}
        prefix_sum = 0
        # c1  = 0
        res = 0

        for i in range(len(nums)):
            if nums[i]:
                prefix_sum += 1

            else:
                prefix_sum -= 1
             
            if prefix_sum not in diffs:
                diffs[prefix_sum] = i

            if prefix_sum == 0:
                res = max(res, i+1)
                
            else:
                pi = diffs[prefix_sum]   #prefix index to remove
                res = max(res, i-pi)

        return res

