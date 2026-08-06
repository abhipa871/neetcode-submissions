class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        memo = {}
        def dp(i):
            if i>=len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        return min(dp(0), dp(1))
                
        '''
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(
                cost[i - 1] + dp[i - 1],
                cost[i - 2] + dp[i - 2]
            )

        return dp[n]