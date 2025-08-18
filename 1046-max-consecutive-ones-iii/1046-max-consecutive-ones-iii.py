from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0,0
        zeros = deque()
        res = 0
        z = 0

        while right < n:
            if nums[right]==0:
                if z<k:
                    z += 1
                    zeros.append(right)
                else:
                    if zeros:
                        last_zero = zeros.popleft()
                        left = last_zero+1
                        zeros.append(right)
                    else:
                        left = right+1

            length = right-left+1
            res = max(res, length)
            right += 1
        return res


        