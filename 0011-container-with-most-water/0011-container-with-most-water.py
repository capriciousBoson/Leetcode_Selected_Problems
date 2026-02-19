class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        res = 0
        while right > left:
            res= max(res, min(height[left], height[right])*(right - left))
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            elif height[left] == height[right]:
                left += 1
                right -= 1
        return res

        
        