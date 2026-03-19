class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffs = {}

        zeros = [0 for _ in nums] 
        ones = [0 for _ in nums]
        c1,c0 = 0,0

        res = 0
        for i in range(len(nums)):
            if nums[i]:
                c1 += 1
                ones[i] = c1
            else:
                c0 += 1
                zeros[i] = c0
            
            if c1-c0 not in diffs:
                diffs[c1-c0] = i

            if c1-c0 == 0:
                res = max(res, i+1)
                
            pi = diffs[c1-c0]   #prefix index to remove
            res = max(res, i-pi)

        return res

