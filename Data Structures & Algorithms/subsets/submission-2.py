class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total = []

        def backtrack(start, res):
            total.append(res[:])
            for i in range(start, len(nums)):
                res.append(nums[i])
                backtrack(i+1, res)
                res.pop()
        backtrack(0, [])
        return total