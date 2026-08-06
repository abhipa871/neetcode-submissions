class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(start, end):
            memo = {}

            def dp(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                rob_current = nums[i] + dp(i + 2)
                skip_current = dp(i + 1)

                memo[i] = max(rob_current, skip_current)
                return memo[i]

            return dp(start)

        # Case 1: include first house, exclude last house
        num1 = rob_range(0, len(nums) - 2)

        # Case 2: exclude first house, allow last house
        num2 = rob_range(1, len(nums) - 1)

        return max(num1, num2)