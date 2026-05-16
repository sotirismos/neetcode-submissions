class Solution:
    def maxArea(self, heights: List[int]) -> int:
        running_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            running_area = max(running_area, current_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return running_area

