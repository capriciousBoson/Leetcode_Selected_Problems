class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        next_greater = {}
        stk = [-1]
        for i in range(len(nums2)-1, -1, -1):
            if stk[-1] > nums2[i]:
                next_greater[nums2[i]] = stk[-1]
                stk.append(nums2[i])
            else:
                while stk[-1] != -1 and stk[-1] <= nums2[i]:
                    stk.pop()
                next_greater[nums2[i]] = stk[-1]
                stk.append(nums2[i])

        return [next_greater[n] for n in nums1]



        