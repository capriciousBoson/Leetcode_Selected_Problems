class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums)%2 != 0: return False
        n = len(nums)
        memo = {}
        def fun(i,x):
            if x==target:
                return True
            if x> target or i>=n:
                return False

            
            if (i,x) not in memo:
                take = fun(i+1, x+nums[i])
                if take:
                    return True
                not_take = fun(i+1, x)
                if not_take:
                    return True
                memo[(i,x)] = take or not_take
            return memo[(i,x)]

        return fun(0,0)

