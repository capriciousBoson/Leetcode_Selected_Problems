class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]

            
        left = 0
        right = len(nums)-1
        

        while left <=right:
            print(nums[left:right+1])
            mid = (left+right) // 2
            print(nums[mid])

            if mid==0:
                if nums[mid] != nums[mid+1]:
                    return nums[mid]
                else:
                    left= mid
                    continue
            elif mid==len(nums)-1:
                if nums[mid-1]!=nums[mid]:
                    return nums[mid]
                else:
                    right = mid
                    continue
            else:
                if nums[mid-1] != nums[mid] != nums[mid+1]:
                    return nums[mid]
                elif nums[mid]==nums[mid-1]:
                    if mid%2:
                        left = mid
                    else:
                        right = mid
                    continue
                elif nums[mid]==nums[mid+1]:
                    if mid%2:
                        right = mid
                    else:
                        left = mid
                    continue

            