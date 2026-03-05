class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        next_greater = {}
        stk = ['/']

        for i in range(len(nums2)-1, -1, -1):
            while stk[-1] != '/' and stk[-1] <= nums2[i]:
                stk.pop()
            next_greater[(i, nums2[i])] = stk[-1]
            stk.append(nums2[i])

        res = []
        for i, n in enumerate(nums):
            ng = next_greater[(i,n)]
            if ng != '/':
                res.append(ng)
            else:
                res.append(-1)

        return res
        