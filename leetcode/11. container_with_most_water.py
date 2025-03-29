from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            # Calculate current area and update max_area if necessary
            current_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
