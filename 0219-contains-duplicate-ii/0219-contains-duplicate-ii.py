class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k : 
            return False
        r = min(len(nums), k)
        found = {}
        for i in range(r):
            if nums[i] in found:
                return True
            else:
                found[nums[i]] = True

        l=0
        while r < len(nums):
            if nums[r] in found and found[nums[r]]==True: 
                return True
            else:
                found[nums[l]] = False
                found[nums[r]] = True
                l += 1
                r += 1
        return False

        
        