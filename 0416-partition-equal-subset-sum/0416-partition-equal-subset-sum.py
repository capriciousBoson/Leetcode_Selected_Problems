class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 !=0 or len(nums) < 2:
            return False

        memo = {}
        def fun(i,target):
            if target==0:
                return True
            if i==0:
                return target==nums[0]

            if (i, target) not in memo:
                take = False
                if target >= nums[i]:
                    take =  fun(i-1, target - nums[i])
                if take==True: return True
                not_take = fun(i-1, target)
                if not_take==True: return True

                memo[(i,target)] = take or not_take
            return memo[(i, target)]
        return fun(len(nums)-1, total//2)