class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        memo = {}
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return memo[i]
        return dfs(0)
        '''
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]