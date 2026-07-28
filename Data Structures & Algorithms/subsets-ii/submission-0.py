class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        total =[]
        nums.sort()
        def backtrack(start, res):
            total.append(res[:])
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                res.append(nums[i])
                backtrack(i+1, res)
                res.pop()
        backtrack(0, [])
        return total
