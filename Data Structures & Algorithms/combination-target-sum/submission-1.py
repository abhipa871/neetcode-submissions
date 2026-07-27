class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = []
        def backtrack(start, res, total_sum):
            if total_sum==target:
                total.append(res[:])
                return 
            if total_sum>target:
                return
            for i in range(start, len(nums)):
                res.append(nums[i])
                backtrack(i, res, nums[i]+total_sum)
                res.pop()
        backtrack(0, [], 0)
        return total