class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr_one = 0
        ptr_two = len(heights)-1
        max_area = 0
        while ptr_one<ptr_two:
            area = min(heights[ptr_one], heights[ptr_two])*(ptr_two-ptr_one)
            max_area=max(area, max_area)
            if heights[ptr_one]<=heights[ptr_two]:
                ptr_one+=1
            elif heights[ptr_two]<heights[ptr_one]:
                ptr_two-=1
        return max_area
            