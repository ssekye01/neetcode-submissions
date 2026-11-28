class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        start = -1
        for i in range(len(heights)):
            start = i 
            while stack and heights[i] < stack[-1][1]:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                start = idx 
            stack.append((start, heights[i]))
        while stack:
            idx, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - idx))
        return max_area
