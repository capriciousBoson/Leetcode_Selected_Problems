class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reached = [False for _ in range(n)]
        reached[0] = True

        for i in range(n):
            if not reached[i]:
                return False
            for j in range(1, nums[i]+1):
                if i + j >=n-1:
                    return True
                reached[i+j] = True
                
        return reached[n-1]


            
