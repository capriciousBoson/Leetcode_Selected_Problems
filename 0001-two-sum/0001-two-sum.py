from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sums = defaultdict(int)
        for i in range(n):
            diff = target - nums[i]
            if diff in sums:
                return [sums[diff], i]
            else:
                sums[nums[i]] = i
        

        