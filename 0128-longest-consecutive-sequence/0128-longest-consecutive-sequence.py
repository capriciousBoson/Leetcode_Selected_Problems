class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        count = 0

        for n in s:
            if n-1 not in s:
                count += 1
                next_element = n+1
                while next_element in s:
                    count += 1
                    next_element = next_element+1
                res = max(res, count)
                count = 0
                
        return res