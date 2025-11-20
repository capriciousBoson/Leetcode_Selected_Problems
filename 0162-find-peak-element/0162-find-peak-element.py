class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n-1
        if n==1: return 0


        while left <= right:
            print(nums[left:right+1])
            mid = (left + right)//2
            print(nums[mid])

            if mid==0 :
                if nums[mid+1] < nums[mid]:
                    return mid
                else:
                    left = mid+1
                    continue
                
            if mid == n-1:
                if nums[mid-1]< nums[mid]:
                    return mid
                else:
                    right = mid-1
                    continue

            if nums[mid-1]< nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid]<=nums[mid+1]:
                left = mid+1
                continue
            else:
                right = mid-1
                continue

            
        