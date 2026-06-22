class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        area = 0
        maxLeft = -1
        maxRight = -1
        while(left<right):
            if(height[left]<height[right]):
                maxLeft = max(height[left], maxLeft)
                area+=maxLeft-height[left]
                left+=1
            else:
                maxRight = max(height[right], maxRight)
                area+=maxRight-height[right]
                right-=1
        return area
