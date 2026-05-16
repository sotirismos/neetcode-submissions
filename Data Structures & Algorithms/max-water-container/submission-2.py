class Solution:
    def maxArea(self, heights: List[int]) -> int:
        running_area = 0
        for i in range(0, len(heights) - 1):
            for j in range(i + 1, len(heights)):
                current_area = (j - i) * min(heights[i], heights[j])
                if current_area > running_area:
                    running_area = current_area
        return running_area

