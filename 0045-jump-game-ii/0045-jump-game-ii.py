class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        j = [float('inf') for _ in range(n)]
        j[0] = 0

        for i in range(n):
            
            for d in range(1,nums[i]+1):
                if i+d<n:
                    j[i+d] = min(1+j[i],j[i+d])
                    if i+d == n-1:
                        return j[i+d]
        return j[n-1]
            
