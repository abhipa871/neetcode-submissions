class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left_smaller = [-1] * n
        right_smaller = [n] * n

        stack = []

        # first smaller to the right
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                right_smaller[index] = i
            stack.append(i)

        stack = []

        # first smaller to the left
        for i in range(n - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                left_smaller[index] = i
            stack.append(i)

        max_area = 0

        for i in range(n):
            width = right_smaller[i] - left_smaller[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area