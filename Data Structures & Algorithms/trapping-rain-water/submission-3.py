class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        max_num = 0
        for i in range(1, len(height)):    
            max_num = max(max_num, height[i-1])
            prefix[i] = max_num
        max_num = 0
        for i in range(len(height)-2, -1, -1):
            max_num = max(max_num, height[i+1])
            suffix[i] = max_num
        sum = 0
        for i in range(len(height)):
            sum+=max(min(prefix[i], suffix[i])-height[i], 0)
        return sum