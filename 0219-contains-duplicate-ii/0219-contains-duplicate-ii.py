class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k : 
            return False
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and abs(i-seen[nums[i]]) <= k:
                return True
            else:
                seen[nums[i]] = i
        return False

        
        