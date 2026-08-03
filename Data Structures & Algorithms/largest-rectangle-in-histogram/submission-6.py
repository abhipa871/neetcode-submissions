class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prefix= [-1]*len(heights)
        suffix = [len(heights)]*len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                suffix[stack[-1]] =i
                stack.pop()
            stack.append(i)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i]<heights[stack[-1]]:
                prefix[stack[-1]] = i
                stack.pop()
            stack.append(i)
        print(prefix)
        print(suffix)
        area = 0
        for i in range(len(prefix)):
            area = max(area, (suffix[i]-prefix[i]-1)*heights[i])
        return area
