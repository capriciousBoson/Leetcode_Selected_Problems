class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        
        res = []
        # lets implement a monotonic queue
        # as we need a running maximum

        q = collections.deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])
        
        left, right = 1, k

        while right < n:
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)
            res.append(nums[q[0]])
            left += 1
            right += 1

        return res




        return res



        