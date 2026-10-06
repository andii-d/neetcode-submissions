class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # water[i] = min(max of left side, max of right side) - height[i]

        l_max = [0] * len(height)
        r_max = [0] * len(height)

        l_max[0] = height[0]
        r_max[-1] = height[-1]

        # Max heights to the left of the current bar
        for i in range(1, len(height)):
            l_max[i] = max(l_max[i-1], height[i])
        
        # Max heights to the right of the current bar
        for i in range(len(height) - 2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])

        # Calculate water based off the above comment's algorithm
        for i in range(len(height)):
            res += min(l_max[i], r_max[i]) - height[i]

        return res