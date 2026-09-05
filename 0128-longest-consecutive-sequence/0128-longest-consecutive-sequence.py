class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in seen:
            if n-1 not in seen:
                count = 1
                next_element = n+1
                while next_element in seen:
                    count += 1
                    next_element += 1
                res = max(res, count)

        return res

        