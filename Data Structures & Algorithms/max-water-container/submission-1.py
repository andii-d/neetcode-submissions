class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float('-inf')
        l, r = 0, len(heights) - 1
        # Calculate the area based off the width and the minimum height between two bars

        while l < r:
            min_height = min(heights[l], heights[r])
            width = r - l
            area = max((width * min_height), area)

            if min(heights[l], heights[r]) == heights[l]:
                l += 1
            elif min(heights[l], heights[r]) == heights[r]:
                r -= 1
                
        return int(area)