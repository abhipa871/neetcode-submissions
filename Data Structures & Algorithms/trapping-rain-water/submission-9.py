class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        area = 0
        max_left = -1
        max_right = -1
        while(left<right):
            if height[left]<height[right]:
                max_left = max(height[left], max_left)
                area+=max_left-height[left]
                left+=1
            else:
                max_right = max(height[right], max_right)
                area+=max_right-height[right]
                right-=1
        return area

