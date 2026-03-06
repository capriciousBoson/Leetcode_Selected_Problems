class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # mse and nse
        min_stk = [-1]
        max_stk = [-1]

        subarr_min_sums = 0 
        subarr_max_sums = 0

        for i in range(len(nums)):
            while min_stk[-1]!= -1 and nums[min_stk[-1]] >= nums[i]:
                idx = min_stk.pop()
                pse = min_stk[-1]   # previous smaller element
                nse = i         # next smaller element

                subarr_min_sums += nums[idx]* (idx-pse) * (nse-idx)
            min_stk.append(i)

            while max_stk[-1] != -1 and nums[max_stk[-1]] <= nums[i]:
                idx = max_stk.pop()
                pge = max_stk[-1]   #previous greater element
                nge = i         #next greater element

                subarr_max_sums += nums[idx]* (idx-pge) * (nge-idx)  
            max_stk.append(i)

        while min_stk:
            idx = min_stk.pop()
            if idx==-1:
                break
            pse = min_stk[-1]
            nse = len(nums)
            subarr_min_sums += nums[idx]* (idx-pse) * (nse-idx)

            

        while max_stk:
            idx = max_stk.pop()
            if idx==-1:
                break
            pge = max_stk[-1]
            nge = len(nums)
            subarr_max_sums += nums[idx]* (idx-pge) * (nge-idx)

        return subarr_max_sums - subarr_min_sums     

        