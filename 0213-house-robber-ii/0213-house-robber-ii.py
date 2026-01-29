class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # edge case:
        if n==1: return nums[0]
        memo = {}

        def rob(i):
            if i>=n:
                return 0
            if i not in memo:
                memo[i] = max(nums[i]+rob(i+2), rob(i+1))
            
            # print(f"memo[{i}] : {memo[i]}")
            return  memo[i]
        
        # skip house 0
        a = rob(1)
        # print(f"a : {a}")

        # rob house zero, skip last one
        memo = {}
        n = n-1
        b = rob(0)
        # print(f"b : {b}")

        return max(a,b)