class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]
        def lowerbound(nums, target):
            lb = 0
            l = 0
            r = len(nums)-1

            while l<=r:
                mid = (l+r)//2

                if nums[mid] >= target:
                    lb = mid
                    r = mid-1
                else:
                    l = mid+1
            return lb
        
        def upperbound(nums, target):
            ub = len(nums)-1
            l = 0
            r = len(nums)-1

            while l<=r:
                mid = (l+r)//2

                if nums[mid]<=target:
                    ub = mid
                    l = mid+1
                else:
                    r = mid-1
            return ub
        lb = lowerbound(nums, target)
        if nums[lb] > target :
            return [-1, -1]
        ub = upperbound(nums, target)
        if nums[ub] < target:
            return [-1, -1]


        return [lb, ub]




