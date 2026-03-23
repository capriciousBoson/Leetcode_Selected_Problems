class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            print(f"i: {i} | nums[i] : {nums[i]} , nums[i-1] = {nums[i-1]}")
            # if nums[i] == '_': break
            if nums[i] == nums[i-1]:
                del nums[i]
                # nums.append('_')
            else:
                i += 1
