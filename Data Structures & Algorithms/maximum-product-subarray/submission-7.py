class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        res = nums[0]
        for i in range(len(nums)):
            temp = curr_max
            curr_max = max(nums[i], temp*nums[i], curr_min*nums[i])
            curr_min = min(nums[i], temp*nums[i], curr_min*nums[i])
            res = max(curr_max, res)
        return res