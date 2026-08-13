class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        for i in range(len(nums)):
            new_dp = set()
            for t in dp:
                if(t+nums[i]==target):
                    return True
                new_dp.add(t+nums[i])
                new_dp.add(t)
            dp = new_dp
        return False
