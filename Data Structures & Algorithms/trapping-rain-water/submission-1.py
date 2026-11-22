class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = -float('inf'), -float('inf')
        total_water = 0
        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
                r -= 1
        return total_water
