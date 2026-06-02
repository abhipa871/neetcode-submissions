class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        prefix = [-1]*len(heights)
        suffix = [len(heights)]*len(heights)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                suffix[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                prefix[stack[-1]] = i
                stack.pop()
            stack.append(i)
        print(prefix)
        print(suffix)
        max_area = 0
        for i in range(len(heights)):
            suff_index = suffix[i]
            pre_index = prefix[i]
            area = (suff_index-pre_index-1) * heights[i]
            max_area = max(area, max_area)


        return max_area