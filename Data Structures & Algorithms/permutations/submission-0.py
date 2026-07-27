class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        total = []
        used = [False] * len(nums)
        res = []

        def backtrack():
            if len(res) == len(nums):
                total.append(res[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                res.append(nums[i])

                backtrack()

                res.pop()
                used[i] = False

        backtrack()
        return total