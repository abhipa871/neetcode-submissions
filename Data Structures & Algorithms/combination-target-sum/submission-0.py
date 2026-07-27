class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = []
        def backtrack(start, res):
            if sum(res)==target:
                total.append(res[:])
                return 
            if sum(res)>target:
                return
            for i in range(start, len(nums)):
                res.append(nums[i])
                backtrack(i, res)
                res.pop()
        backtrack(0, [])
        return total