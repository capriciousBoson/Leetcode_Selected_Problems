class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)-1
        if n==0 : return True

        i = 0
        max_jump = nums[i]
        while i <= n:
            if i > max_jump: return False
            max_jump = max(i+nums[i], max_jump)
            i += 1       
        return True   