from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0,0
        # zeros = deque()
        res = 0
        z = 0

        while right < n:
            if nums[right]==0:
                z+= 1
            while z > k:
                if nums[left] == 0:
                    z -= 1
                left += 1
                

            res = max(res, right-left+1)
            right += 1
        return res


        