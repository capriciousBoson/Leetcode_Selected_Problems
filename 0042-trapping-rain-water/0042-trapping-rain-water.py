class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) -1
        leftmax = height[l]
        rightmax = height[r]

        while l < r:
            if leftmax <= rightmax:
                l += 1
                if height[l] < leftmax:
                    res += leftmax - height[l]
                leftmax = max(leftmax, height[l])
            elif rightmax < leftmax:
                r -= 1
                if height[r] < rightmax:
                    res += rightmax - height[r]
                rightmax = max(rightmax, height[r])
        return res


            
            
        
            

        