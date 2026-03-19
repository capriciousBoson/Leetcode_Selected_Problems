class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffs = {}

        c1  = 0
        res = 0

        for i in range(len(nums)):
            if nums[i]:
                c1 += 1

            c0 = i-c1+1
            
            if c1-c0 not in diffs:
                diffs[c1-c0] = i

            if c1-c0 == 0:
                res = max(res, i+1)
                
            else:
                pi = diffs[c1-c0]   #prefix index to remove
                res = max(res, i-pi)

        return res

