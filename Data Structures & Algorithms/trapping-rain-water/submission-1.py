class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        max_num = 0
        for i in range(len(height)):
            if i==0:
                prefix[i] = 0
            else:
                if height[i-1]>=max_num:
                    max_num = height[i-1]
                prefix[i] = max_num
        print(prefix)
        max_num = 0
        for i in range(len(height)-1, -1, -1):
            if i==len(height)-1:
                suffix[i] = 0
            else:
                if height[i+1]>=max_num:
                    max_num = height[i+1]
                suffix[i] = max_num
        print(suffix)
        sum = 0
        for i in range(len(height)):
            sum+=max(min(prefix[i], suffix[i])-height[i], 0)
        return sum