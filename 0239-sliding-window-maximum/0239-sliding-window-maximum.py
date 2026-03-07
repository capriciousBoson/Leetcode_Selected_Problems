class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        res = []
        # we implement a monotonic queue
        q = collections.deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])
            

        left = 1
        right = k

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if q[0] < left:
                q.popleft()
            
            res.append(nums[q[0]])

            left += 1
            right += 1
        
        return res


        