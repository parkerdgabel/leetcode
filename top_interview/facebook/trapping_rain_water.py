from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    ans = ans + (max_left - height[left])
                left = left + 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    ans = ans + (max_right - height[right])
                right = right - 1
        return ans