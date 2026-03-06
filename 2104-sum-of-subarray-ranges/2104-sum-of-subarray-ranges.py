class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # mse and nse
        stk = [-1]
        subarr_min_sums = 0 
        subarr_max_sums = 0

        for i in range(len(nums)):
            while stk[-1]!= -1 and nums[stk[-1]] >= nums[i]:
                idx = stk.pop()
                pse = stk[-1]   # previous smaller element
                nse = i         # next smaller element

                subarr_min_sums += nums[idx]* (idx-pse) * (nse-idx)
            stk.append(i)

        while stk:
            idx = stk.pop()
            if idx==-1:
                break
            pse = stk[-1]
            nse = len(nums)
            subarr_min_sums += nums[idx]* (idx-pse) * (nse-idx)


        
        stk = [-1]
        for i in range(len(nums)):
            while stk[-1] != -1 and nums[stk[-1]] <= nums[i]:
                idx = stk.pop()
                pge = stk[-1]   #previous greater element
                nge = i         #next greater element

                subarr_max_sums += nums[idx]* (idx-pge) * (nge-idx)  
            stk.append(i)

        while stk:
            idx = stk.pop()
            if idx==-1:
                break
            pge = stk[-1]
            nge = len(nums)
            subarr_max_sums += nums[idx]* (idx-pge) * (nge-idx)

        return subarr_max_sums - subarr_min_sums     

        