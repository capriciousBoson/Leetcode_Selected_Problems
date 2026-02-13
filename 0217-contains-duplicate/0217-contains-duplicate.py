class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen:
                return True
            else:
                seen[n]=1
        return False
        