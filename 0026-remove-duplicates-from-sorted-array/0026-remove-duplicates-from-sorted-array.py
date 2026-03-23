class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return len(nums)

        l = 1
        r = 1 

        while r < len(nums): 
            # if element alr seen
            if nums[r] == nums[r-1]: 
                r += 1
            # new element 
            else: 
                nums[l] = nums[r]
                l += 1
                r += 1
        
        return l
        
        # Time: O(n) - because r moves 1 each time so it visits every element in nums once
        # Memory: O(1) - for the two pointersn(nums):

