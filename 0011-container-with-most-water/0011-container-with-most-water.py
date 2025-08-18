class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        left, right = 0, len(height)-1

        while left < right:
            water = min(height[left], height[right]) * (right-left)
            res = max(res, water)

            if height[left]<height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return res
        