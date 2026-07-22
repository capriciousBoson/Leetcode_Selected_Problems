class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def subsetXOR(x, i):
            nonlocal res
            if i>= len(nums):
                res += x
                return
            
            subsetXOR(x, i+1)
            subsetXOR(x^nums[i], i+1)
            return
        
        subsetXOR(0,0)
        return res
        