class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        n = len(nums)

        for i in range(n):
            res.append(prefix)
            prefix = prefix*nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i]*postfix
            postfix = postfix*nums[i]
        return res
        