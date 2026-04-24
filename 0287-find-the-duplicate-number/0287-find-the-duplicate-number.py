class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)<3:
            return nums[0]
        for n in nums:
            ind = abs(n)
            if nums[ind] < 0:
                return ind
            nums[ind] = -1 * nums[ind]