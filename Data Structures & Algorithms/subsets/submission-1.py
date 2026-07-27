class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(remaining, curr):
            ans.append(curr[:])

            for i, num in enumerate(remaining):
                curr.append(num)
                backtrack(remaining[i + 1:], curr)
                curr.pop()

        backtrack(nums, [])
        return ans