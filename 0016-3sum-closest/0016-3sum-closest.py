class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0

        nums.sort()

        n = len(nums)
        diff = float('inf')

        for i in range(n-2):
            # if i >0 and nums[i]==nums[i+1]:
            #     continue
            
            l,r = i+1, n-1
            while l<r:
                x = nums[i]+nums[l]+nums[r]
                if x==target:
                    return x
                
                if diff > abs(target-x):
                    diff = abs(target-x)
                    res = x

                if x < target:
                    l += 1
                elif x>target:
                    r -= 1
        
        return res