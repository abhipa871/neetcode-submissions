class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = defaultdict(lambda:1)
        max_num = 1
        def dp(i):
            if i==len(nums):
                return 1
            if i in memo:
                return memo[i]
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    memo[i] = max(memo[i], 1+dp(j))

            return memo[i]
        for i in range(len(nums)):
            max_num = max(max_num, dp(i))
        return max_num

            
